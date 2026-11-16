import argparse
import io
import json
import re
import subprocess
import zipfile
import zlib
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Scan reachable Git blobs and ZIP members without printing matched values."
)
parser.add_argument(
    "--output",
    type=Path,
    default=Path("AnalyseFuture/recovery/security/SECURITY_SCAN_RESULTS.json"),
)
args = parser.parse_args()
ROOT = Path(__file__).resolve().parents[2]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


scan_head = git("rev-parse", "HEAD").decode().strip()
scan_commits = len(git("rev-list", "--all").splitlines())
lines = git("rev-list", "--objects", "--all").decode().splitlines()
paths = {
    line.split(" ", 1)[0]: line.split(" ", 1)[1] if " " in line else "<commit/tree>"
    for line in lines
}
meta = (
    subprocess.run(
        ["git", "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"],
        cwd=ROOT,
        input=("\n".join(paths) + "\n").encode(),
        stdout=subprocess.PIPE,
        check=True,
    )
    .stdout.decode()
    .splitlines()
)
blobs = [(v.split()[0], int(v.split()[2])) for v in meta if v.split()[1] == "blob"]
patterns = {
    "private_key": rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    "github_token": rb"(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})",
    "openai_style": rb"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}",
    "aws_access_id": rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "google_api": rb"\bAIza[A-Za-z0-9_-]{30,}",
    "stripe_live": rb"\b(?:sk|rk)_live_[A-Za-z0-9]{16,}",
    "slack_token": rb"\bxox[baprs]-[A-Za-z0-9-]{20,}",
    "jwt_literal": rb"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{16,}",
    "url_userinfo": rb'https?://[^\s/:"\x27]{2,}:[^\s/@"\x27]{2,}@',
}
compiled = {k: re.compile(v) for k, v in patterns.items()}
findings = []
zip_count = 0
zip_members = 0
binary = 0
text = 0
total = 0
errors = []


def scan(data, path, oid, archived=False):
    global text, binary
    try:
        data.decode("utf-8")
        text += 1
    except UnicodeDecodeError:
        binary += 1
    for name, pat in compiled.items():
        for m in pat.finditer(data):
            findings.append(
                {
                    "pattern": name,
                    "path": path,
                    "oid": oid,
                    "line": data.count(b"\n", 0, m.start()) + 1,
                    "length": m.end() - m.start(),
                }
            )


batch = subprocess.run(
    ["git", "cat-file", "--batch"],
    cwd=ROOT,
    input=("\n".join(oid for oid, _ in blobs) + "\n").encode(),
    stdout=subprocess.PIPE,
    check=True,
).stdout
pos = 0
for oid, size in blobs:
    end = batch.index(b"\n", pos)
    header = batch[pos:end].split()
    assert header[0].decode() == oid and header[1] == b"blob" and int(header[2]) == size
    pos = end + 1
    data = batch[pos : pos + size]
    assert len(data) == size and batch[pos + size : pos + size + 1] == b"\n"
    pos += size + 1
    total += len(data)
    p = paths[oid]
    scan(data, p, oid)
    if data[:4] == b"PK\x03\x04":
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                zip_count += 1
                for f in z.infolist():
                    if f.is_dir():
                        continue
                    zip_members += 1
                    scan(z.read(f), p + "!" + f.filename, oid, True)
        except (
            zipfile.BadZipFile,
            RuntimeError,
            ValueError,
            OSError,
            EOFError,
            zlib.error,
        ) as e:
            errors.append({"oid": oid, "path": p, "error": type(e).__name__})
result = {
    "commits": scan_commits,
    "objects": len(paths),
    "unique_blobs": len(blobs),
    "blob_bytes": total,
    "zip_blobs": zip_count,
    "zip_members_scanned": zip_members,
    "utf8_scans": text,
    "non_utf8_scans": binary,
    "patterns": list(patterns),
    "findings": findings,
    "errors": errors,
}
result["head"] = scan_head
result["worktree_paths_scanned"] = 0
for rel in git("ls-files", "-z").decode().split("\0"):
    if not rel:
        continue
    scan((ROOT / rel).read_bytes(), rel, "working-tree")
    result["worktree_paths_scanned"] += 1
result["findings"] = findings
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(1 if findings or errors else 0)
