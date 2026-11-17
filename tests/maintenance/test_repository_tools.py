"""Exercise real maintenance CLIs in disposable local Git fixtures, never the app."""

import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

SOURCE_ROOT = Path(__file__).resolve().parents[2]


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", *args],
        cwd=repo,
        text=True,
    ).strip()


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repository with spaces"
    root.mkdir()
    git(root, "init", "--quiet", "--initial-branch=main", "--template=")
    git(root, "config", "user.name", "Module test fixture")
    git(root, "config", "user.email", "fixture@example.invalid")
    scripts = root / "scripts/maintenance"
    scripts.mkdir(parents=True)
    for name in ("repository_inventory.py", "security_history_scan.py"):
        shutil.copyfile(SOURCE_ROOT / "scripts/maintenance" / name, scripts / name)
    (root / "README.md").write_text("# Fixture documentation\n")
    source = root / "services/voice-agent/src/eng_teacher/teaching"
    source.mkdir(parents=True)
    (source / "example.py").write_text(
        'import math\nraise RuntimeError("must never import fixture source")\n'
    )
    (root / "payload.bin").write_bytes(b"\0\xff\x00")
    for feature in ("avatar", "practice", "pronunciation"):
        web_feature = root / "apps/web/features" / feature
        web_feature.mkdir(parents=True)
        (web_feature / "feature.ts").write_text("export {};\n")
    git(root, "add", ".")
    git(root, "commit", "--quiet", "-m", "synthetic fixture")
    return root


def run_tool(repo: Path, tool: str, output: Path, *args: str):
    return subprocess.run(
        [
            sys.executable,
            str(repo / "scripts/maintenance" / tool),
            "--output",
            str(output),
            *args,
        ],
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )


def test_inventory_covers_staged_paths_and_does_not_import_source(repo, tmp_path):
    original_head = git(repo, "rev-parse", "HEAD")
    (repo / "staged.txt").write_text("New tracked work\n")
    (repo / "untracked.txt").write_text("Must not be inventoried\n")
    git(repo, "add", "staged.txt")
    output = tmp_path / "inventory.txt"
    result = run_tool(
        repo, "repository_inventory.py", output, "--baseline", original_head
    )
    assert result.returncode == 0, result.stderr
    text = output.read_text()
    paths = {line[6:] for line in text.splitlines() if line.startswith("PATH: ")}
    assert paths == set(git(repo, "ls-files").splitlines())
    assert "untracked.txt" not in paths
    assert "staged.txt" in paths
    assert "Teaching policy and learner controls" in text
    assert "Remote teacher avatar and audio analysis" in text
    assert "Standalone English practice and feedback" in text
    assert "Local microphone recording and self-listening" in text
    assert "binary" in text
    assert original_head in text


def test_inventory_ref_reads_immutable_payloads(repo, tmp_path):
    original_head = git(repo, "rev-parse", "HEAD")
    original = (repo / "README.md").read_bytes()
    (repo / "README.md").write_text("Changed working payload\n")
    output = tmp_path / "historical.txt"
    result = run_tool(repo, "repository_inventory.py", output, "--ref", original_head)
    assert result.returncode == 0, result.stderr
    row = output.read_text().split("PATH: README.md\n", 1)[1].split("\nPATH: ", 1)[0]
    assert hashlib.sha256(original).hexdigest() in row
    assert hashlib.sha256((repo / "README.md").read_bytes()).hexdigest() not in row


def test_inventory_missing_git_root_fails_instead_of_claiming_coverage(repo, tmp_path):
    not_a_repo = tmp_path / "no git metadata"
    not_a_repo.mkdir()
    result = run_tool(
        repo,
        "repository_inventory.py",
        tmp_path / "none.txt",
        "--root",
        str(not_a_repo),
    )
    assert result.returncode != 0


def test_history_scanner_reports_clean_real_git_fixture(repo, tmp_path):
    output = tmp_path / "scan.json"
    result = run_tool(repo, "security_history_scan.py", output)
    assert result.returncode == 0, result.stderr
    data = json.loads(output.read_text())
    assert data["head"] == git(repo, "rev-parse", "HEAD")
    assert data["commits"] == 1
    assert data["worktree_paths_scanned"] == len(git(repo, "ls-files").splitlines())
    assert data["findings"] == data["errors"] == []


def test_scanner_detects_new_staged_candidate_without_printing_value(repo, tmp_path):
    synthetic = "sk-" + "x" * 32
    (repo / "candidate.txt").write_text(synthetic)
    git(repo, "add", "candidate.txt")
    output = tmp_path / "staged-scan.json"
    result = run_tool(repo, "security_history_scan.py", output)
    data = json.loads(output.read_text())
    assert result.returncode == 1
    assert any(item["oid"] == "working-tree" for item in data["findings"])
    assert synthetic not in result.stdout + result.stderr + output.read_text()


def test_scanner_keeps_historical_evidence_after_value_is_replaced(repo, tmp_path):
    synthetic = "sk-" + "x" * 32
    (repo / "candidate.txt").write_text(synthetic)
    git(repo, "add", "candidate.txt")
    git(repo, "commit", "--quiet", "-m", "synthetic candidate")
    (repo / "candidate.txt").write_text("redacted fixture\n")
    git(repo, "add", "candidate.txt")
    output = tmp_path / "historical-scan.json"
    result = run_tool(repo, "security_history_scan.py", output)
    data = json.loads(output.read_text())
    assert result.returncode == 1
    assert any(item["oid"] != "working-tree" for item in data["findings"])
    assert synthetic not in result.stdout + result.stderr + output.read_text()


def test_scanner_reads_zip_members_without_extracting_or_printing_values(
    repo, tmp_path
):
    synthetic = "sk-" + "x" * 32
    with zipfile.ZipFile(repo / "fixture.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("nested/candidate.txt", synthetic)
    git(repo, "add", "fixture.zip")
    git(repo, "commit", "--quiet", "-m", "synthetic archive")
    output = tmp_path / "zip-scan.json"
    result = run_tool(repo, "security_history_scan.py", output)
    data = json.loads(output.read_text())
    assert result.returncode == 1
    assert data["zip_members_scanned"] == 1
    assert any("!nested/candidate.txt" in item["path"] for item in data["findings"])
    assert not (repo / "nested").exists()
    assert synthetic not in result.stdout + result.stderr + output.read_text()


def test_corrupt_zip_is_a_failed_scan_not_a_false_clean_result(repo, tmp_path):
    (repo / "broken.zip").write_bytes(b"PK\x03\x04")
    git(repo, "add", "broken.zip")
    git(repo, "commit", "--quiet", "-m", "synthetic unreadable archive")
    output = tmp_path / "bad-zip-scan.json"
    result = run_tool(repo, "security_history_scan.py", output)
    data = json.loads(output.read_text())
    assert result.returncode == 1
    assert data["errors"] and data["errors"][0]["error"] == "BadZipFile"
