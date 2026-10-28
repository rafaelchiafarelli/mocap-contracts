"""`make gen` on a clean tree gives no diff: regenerate into a temp dir and
compare with what is committed. Skipped where Harpia can't run (no Docker or
no submodule checkout)."""

import filecmp
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ["gen/python", "gen/java", "schema/schema_registry", "mocap_contracts/messages.py",
             "mocap_contracts/zmq_endpoints.py"]


def _docker_ok():
    if not shutil.which("docker"):
        return False
    return subprocess.run(["docker", "info"], capture_output=True).returncode == 0


pytestmark = pytest.mark.skipif(
    not (ROOT / "third_party/harpia/Docker/run.sh").exists() or not _docker_ok(),
    reason="needs the Harpia submodule and a running Docker",
)


def _files(root: Path) -> set[Path]:
    # Files only: git keeps no empty folders, and Harpia's Java run makes some
    # (gen/java/src/test, generated/{db,rest,soap}), so a fresh clone lacks them.
    if root.is_file():
        return {Path()}
    return {p.relative_to(root) for p in root.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts}


def _diff(a: Path, b: Path) -> list[str]:
    fa, fb = _files(a), _files(b)
    out = [f"only in one side: {a / p}" for p in sorted(fa ^ fb)]
    out += [str(a / p) for p in sorted(fa & fb)
            if not filecmp.cmp(a / p, b / p, shallow=False)]
    return out


def test_regeneration_matches_committed(tmp_path):
    subprocess.run([sys.executable, str(ROOT / "tools/harpia_gen.py"), "--into", str(tmp_path)],
                   check=True, capture_output=True)
    diffs = [d for rel in GENERATED for d in _diff(ROOT / rel, tmp_path / rel)]
    assert not diffs, diffs
