"""Run Gradle on the generated Java (gen/java) in the official Gradle image.

`gradle:8.7-jdk17` with host networking, so a Java peer can reach a Python
socket on 127.0.0.1. Staging and the Gradle cache live under build/
(gitignored). Slow tests only.
"""

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "gradle:8.7-jdk17@sha256:4ad3845d9ee2843537747bd5f067cc6c7a18e737d0079a880a5a074feda392a4"
STAGE = ROOT / "build" / "java-test"
CACHE = ROOT / "build" / "gradle-cache"

SLOW = os.environ.get("MOCAP_SLOW_TESTS") == "1"
SKIP_REASON = "slow (Gradle in Docker): run with `make test-slow` or MOCAP_SLOW_TESTS=1"


def docker_ok() -> bool:
    return bool(shutil.which("docker")) and subprocess.run(["docker", "info"], capture_output=True).returncode == 0


def stage_java(extra: dict[str, str] | None = None) -> Path:
    """Copy gen/java to build/java-test/java, plus extra files (relative path → text)."""
    if STAGE.exists():
        shutil.rmtree(STAGE)
    shutil.copytree(ROOT / "gen" / "java", STAGE / "java")
    for rel, text in (extra or {}).items():
        path = STAGE / "java" / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    return STAGE / "java"


def gradle(args: str, timeout: int = 900) -> subprocess.CompletedProcess:
    CACHE.mkdir(parents=True, exist_ok=True)
    cmd = [
        "docker", "run", "--rm", "--network", "host", "-u", f"{os.getuid()}:{os.getgid()}",
        "-e", "GRADLE_USER_HOME=/cache", "-v", f"{STAGE}:/work", "-v", f"{CACHE}:/cache",
        "-w", "/work/java", IMAGE, "bash", "-c", f"gradle --no-daemon -q {args}",
    ]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
