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
GENERATED = ["gen/python", "schema/schema_registry", "mocap_contracts/messages.py",
             "mocap_contracts/zmq_endpoints.py"]


def _docker_ok():
    if not shutil.which("docker"):
        return False
    return subprocess.run(["docker", "info"], capture_output=True).returncode == 0


pytestmark = pytest.mark.skipif(
    not (ROOT / "third_party/harpia/Docker/run.sh").exists() or not _docker_ok(),
    reason="needs the Harpia submodule and a running Docker",
)


def _diff(a: Path, b: Path) -> list[str]:
    if a.is_file():
        return [] if filecmp.cmp(a, b, shallow=False) else [str(a)]
    cmp = filecmp.dircmp(a, b, ignore=["__pycache__"])
    out = [f"only in one side: {p}" for p in cmp.left_only + cmp.right_only]
    out += [str(a / p) for p in cmp.diff_files + cmp.funny_files]
    for sub in cmp.common_dirs:
        out += _diff(a / sub, b / sub)
    return out


def test_regeneration_matches_committed(tmp_path):
    subprocess.run([sys.executable, str(ROOT / "tools/harpia_gen.py"), "--into", str(tmp_path)],
                   check=True, capture_output=True)
    diffs = [d for rel in GENERATED for d in _diff(ROOT / rel, tmp_path / rel)]
    assert not diffs, diffs
