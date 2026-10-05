import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _deps(path):
    return sorted(tomllib.loads(path.read_text())["project"]["dependencies"])


def test_runtime_deps_match_the_generated_package():
    assert _deps(ROOT / "pyproject.toml") == _deps(ROOT / "gen/python/pyproject.toml")
