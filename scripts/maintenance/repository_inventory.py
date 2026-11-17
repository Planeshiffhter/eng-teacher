"""Read tracked files without importing them; emit an auditable ownership inventory."""

from __future__ import annotations

import argparse
import ast
import hashlib
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(root), *args])


def ownership(path: str) -> tuple[str, str, str]:
    if path.startswith(
        "AnalyseFuture/original-projects/reference-sources/Cadence-main/"
    ):
        rel = path.split("/Cadence-main/", 1)[1]
        area = rel.split("/")[0]
        if rel.startswith("src/backend/"):
            area = "/".join(rel.split("/")[:3])
        elif rel.startswith("src/app/api/"):
            area = "/".join(rel.split("/")[:5])
        elif rel.startswith("src/lib/"):
            area = "/".join(rel.split("/")[:3])
        return (
            "Cadence reference: " + area,
            "archived; not an active dependency",
            "retain for selective future evaluation",
        )
    if path.startswith(
        "AnalyseFuture/original-projects/reference-sources/talking-avatar-master/"
    ):
        return (
            "Avatar SDK reference",
            "archived; not an active dependency",
            "retain SDK/model/assets with notices",
        )
    if path.startswith("AnalyseFuture/original-projects/"):
        return (
            "Original upload and import provenance",
            "preserved source input/archive, not execution",
            "keep complete project wrapper and ZIP relationships",
        )
    if path.startswith("AnalyseFuture/historical-implementations/"):
        return (
            "Pre-consolidation tutor",
            "archived baseline; superseded",
            "compare with recovered active tutor",
        )
    if path.startswith("AnalyseFuture/recovery/"):
        category = path.split("/")[2]
        return (
            "Recovery " + category,
            "historical evidence or current maintenance metadata",
            "retain by report responsibility",
        )
    if path.startswith("AnalyseFuture/future-ideas/"):
        return (
            "Future product vision",
            "planning, not implemented product",
            "retain speculative scope separately",
        )
    if path.startswith("AnalyseFuture/"):
        return (
            "Recovery evidence and future work",
            "documentation/data; not application execution",
            "retain audit provenance",
        )
    if path.startswith("apps/web/features/lesson/") or path in {
        "apps/web/components/tutor-app.tsx",
        "apps/web/lib/tutor-events.ts",
        "apps/web/tests/tutor-events.test.ts",
    }:
        return (
            "Live lesson UI and events",
            "active web feature",
            "apps/web/features/lesson",
        )
    if path.startswith("apps/web/features/session/") or path in {
        "apps/web/lib/server/session.ts",
        "apps/web/tests/server-session.test.ts",
        "apps/web/app/api/session/route.ts",
    }:
        return (
            "Session admission and token signing",
            "active server feature",
            "feature module with thin Next.js API route",
        )
    if path.startswith("apps/web/features/avatar/"):
        return (
            "Remote teacher avatar and audio analysis",
            "optional active web feature",
            "apps/web/features/avatar",
        )
    if path.startswith(("apps/web/features/practice/", "apps/web/app/practice/")):
        return (
            "Standalone English practice and feedback",
            "active web feature with a thin Next.js page",
            "apps/web/features/practice",
        )
    if path.startswith("apps/web/features/pronunciation/"):
        return (
            "Local microphone recording and self-listening",
            "optional active web feature",
            "apps/web/features/pronunciation",
        )
    if path.startswith("apps/web/"):
        return (
            "Web shell/build configuration",
            "active web application",
            "keep framework conventions",
        )
    if path.startswith("services/voice-agent/src/eng_teacher/teaching/"):
        return (
            "Teaching policy and learner controls",
            "active Python teaching module",
            "teaching",
        )
    if path.startswith("services/voice-agent/src/eng_teacher/runtime/"):
        return "Voice runtime and lifecycle", "active LiveKit worker", "runtime"
    if path.startswith("services/voice-agent/src/eng_teacher/providers/"):
        return "Speech/text provider adapters", "active provider boundary", "providers"
    if path.startswith("services/voice-agent/tests/"):
        return (
            "Voice fixtures: " + path.split("/")[3],
            "active service verification fixtures; execution recorded in validation reports",
            "tests grouped by matching runtime/teaching owner",
        )
    if path.startswith("services/voice-agent/"):
        return (
            "Voice tutor: " + Path(path).stem,
            "active Python service",
            "services/voice-agent",
        )
    if path.startswith("tests/maintenance/"):
        return (
            "Repository maintenance regression fixtures",
            "active CLI fixtures using disposable Git repositories",
            "tests/maintenance",
        )
    if path.startswith("tests/contracts/"):
        return (
            "Cross-runtime lesson contract",
            "active verification fixture, not runtime curriculum",
            "tests/contracts",
        )
    if path.startswith("tests/"):
        return "Cross-component browser smoke", "active scoped tests", "tests/browser"
    if path.startswith("scripts/"):
        return "Repository maintenance", "explicit maintenance command", "scripts"
    if path.startswith(".github/"):
        return (
            "Continuous integration",
            "active root workflow",
            "explicit active-project targets only",
        )
    if path in {"README.md", "PROJECT_STRUCTURE.md", "AGENTS.md"}:
        return (
            "Repository navigation and working agreement",
            "maintainer documentation",
            "root entrypoint",
        )
    if path.startswith("docs/"):
        return (
            "Documentation: " + path.split("/")[1],
            "documentation, not implementation",
            "retain by product/architecture/development/research/continuity/legal purpose",
        )
    if path.endswith((".md", ".txt")):
        return (
            "Project research and specification",
            "documentation, not implementation",
            "retain canonical history and evidence",
        )
    return (
        "Workspace/build configuration",
        "root configuration",
        "retain supported tool entrypoint",
    )


def describe(path: str, text: str | None) -> tuple[str, list[str], list[str]]:
    name = Path(path).name
    if text is None:
        return (
            "Binary asset/archive; bytes hashed, not executed or semantically decoded",
            [],
            [],
        )
    imports: list[str] = []
    symbols: list[str] = []
    if path.endswith(".py"):
        try:
            tree = ast.parse(text)
            imports = sorted(
                {
                    n.module or "."
                    for n in ast.walk(tree)
                    if isinstance(n, ast.ImportFrom)
                }
                | {
                    a.name
                    for n in ast.walk(tree)
                    if isinstance(n, ast.Import)
                    for a in n.names
                }
            )
            symbols = [
                n.name
                for n in tree.body
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
            ]
        except SyntaxError:
            symbols = ["static-parse-error; manual review required"]
    elif path.endswith((".ts", ".tsx", ".js", ".mjs", ".cjs")):
        imports = sorted(
            set(
                re.findall(
                    r"(?:from\s*|import\s*|require\s*\()\s*['\"]([^'\"\n]+)['\"]", text
                )
            )
        )
        symbols = re.findall(
            r"(?:export\s+)?(?:async\s+)?(?:function|class|interface|type)\s+(\w+)",
            text,
        )
    if "/tests/" in path or "/test/" in path or re.search(r"\.(?:test|spec)\.", path):
        purpose = "Test/fixture for " + Path(path).stem
    elif name in {"package.json", "pyproject.toml", "requirements.txt"}:
        purpose = (
            "Package, dependency and command declarations for its containing component"
        )
    elif name.endswith(("lock.json", "lock.yaml")) or name == "uv.lock":
        purpose = "Resolved dependency versions/integrity; not an independent feature"
    elif name in {"LICENSE", "NOTICE", "CREDITS.md"}:
        purpose = (
            "Licensing/attribution evidence; preserve with related source and assets"
        )
    elif path.endswith((".md", ".txt")):
        purpose = (
            "Documentation: "
            + next(
                (s.lstrip("# ").strip() for s in text.splitlines() if s.strip()), name
            )[:150]
        )
    elif symbols:
        purpose = "Defines " + ", ".join(symbols[:12])
    elif path.endswith(".json"):
        purpose = "Structured configuration/content/fixture: " + name
    else:
        purpose = "Component resource/configuration: " + name
    return purpose, imports, symbols


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[2]
    )
    parser.add_argument(
        "--ref", help="Inspect an immutable Git tree instead of working files"
    )
    parser.add_argument(
        "--baseline", default="HEAD", help="Git tree whose initial count is recorded"
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    baseline = git(root, "rev-parse", args.baseline).decode().strip()
    baseline_count = len(
        git(root, "ls-tree", "-r", "--name-only", args.baseline).splitlines()
    )
    paths = (
        (
            git(root, "ls-tree", "-r", "--name-only", "-z", args.ref)
            if args.ref
            else git(root, "ls-files", "-z")
        )
        .decode()
        .rstrip("\0")
        .split("\0")
    )
    rows = []
    hashes: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        raw = (
            git(root, "show", args.ref + ":" + path)
            if args.ref
            else (root / path).read_bytes()
        )
        try:
            text = raw.decode("utf-8") if b"\0" not in raw else None
        except UnicodeDecodeError:
            text = None
        digest = hashlib.sha256(raw).hexdigest()
        hashes[digest].append(path)
        rows.append((path, raw, text, digest, ownership(path), describe(path, text)))
    lines = [
        "COMPLETE TRACKED FILE INVENTORY",
        "",
        f"Baseline commit: {baseline} ({baseline_count:,} paths)",
        "Inventory source: "
        + (args.ref or "current tracked index paths; current working payloads"),
        f"Tracked paths classified: {len(rows)}",
        "Every listed payload was read; text parsed statically where supported; no imported code was executed.",
        "Binary assets are byte-inventoried, not claims of model/media semantic verification.",
        "Imports are static, partial evidence; dynamic references require component review.",
        "Generated recovery reports omit sizes/digests to avoid circular self-inventory claims.",
        "Feature/duplicate/security reports provide semantic review and runtime boundaries.",
        "",
    ]
    for path, raw, text, digest, owner, detail in rows:
        feature, active, recommendation = owner
        purpose, imports, _symbols = detail
        generated = (
            path.startswith("AnalyseFuture/")
            and path.endswith(".txt")
            and "/reference-sources/" not in path
        )
        copies = [p for p in hashes[digest] if p != path]
        lines.extend(
            [
                "PATH: " + path,
                "  Owner: " + feature,
                "  Purpose: " + purpose,
                "  Use/status: " + active,
                "  Format: "
                + ("UTF-8 text" if text is not None else "binary")
                + (
                    "; generated report (digest/size omitted)"
                    if generated
                    else f"; bytes={len(raw)}; sha256={digest}"
                ),
                "  Dependencies: "
                + (
                    ", ".join(imports)
                    if imports
                    else "no static imports found / see containing component manifest"
                ),
                "  Duplicate evidence: "
                + (
                    "byte-identical to " + "; ".join(copies)
                    if copies
                    else "no exact tracked-payload duplicate; semantic overlap assessed separately"
                ),
                "  Recommendation/location: " + recommendation,
                "",
            ]
        )
    lines.extend(
        [
            "SUMMARY",
            *[
                f"{kind}: {count}"
                for kind, count in sorted(
                    Counter(
                        "UTF-8 text" if r[2] is not None else "binary" for r in rows
                    ).items()
                )
            ],
            "",
            "ADDITIONAL ACCESSIBLE BRANCH-HEAD PATHS AT DISCOVERY",
            "docs/research/TWO_PRIMARY_REFERENCE_REPOS.md — retry branch da2796e; pinned research recovered into canonical docs during consolidation.",
            "Older MVP branch fa600a6 has no unique head path missing from the starting main tree.",
            "All historical payload versions remain reachable through fetched branches and the backup tag; this report does not duplicate each revision of each file.",
            "",
        ]
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Inventoried {len(rows)} paths into {args.output}")


if __name__ == "__main__":
    main()
