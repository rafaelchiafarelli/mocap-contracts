"""The session folder layout, identical on the recorder PC and the processing PC.

    <root>/<session>/session.json
    <root>/<session>/calibration/calibration.toml
    <root>/<session>/takes/<take>/take.json, report.json, closed.json
                                 raw/<role>.mkv, raw/<role>.timestamps.csv
                                 prep/<role>.mkv
                                 extract/index.json, quality.json, quality.md, synced/<role>.mp4
                                 adapt/mocap_take.json
                                 blender/
    <file>.ready.json            next to the file it announces (CameraFileReady)

Paths only: nothing here creates folders or touches files. Stdlib only.
"""

from __future__ import annotations

import re
from pathlib import Path

from mocap_contracts.errors import ContractError

ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")

# Header of every <role>.timestamps.csv: one row per frame, host clock in ns.
TIMESTAMPS_COLUMNS = ("frame", "host_ts_ns")


def check_id(kind: str, value: str) -> str:
    """Return value if it can be a folder or file name, else raise ContractError."""
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise ContractError(
            f"invalid {kind} id {value!r}: letters, digits, '-' and '_', starting with "
            "a letter or digit, at most 64 characters"
        )
    return value


# ---------------------------------------------------------------- session

def session_dir(root: Path | str, session: str) -> Path:
    return Path(root) / check_id("session", session)


def session_json(root: Path | str, session: str) -> Path:
    return session_dir(root, session) / "session.json"


def calibration_dir(root: Path | str, session: str) -> Path:
    return session_dir(root, session) / "calibration"


def calibration_toml(root: Path | str, session: str) -> Path:
    return calibration_dir(root, session) / "calibration.toml"


# ---------------------------------------------------------------- take

def take_dir(root: Path | str, session: str, take: str) -> Path:
    return session_dir(root, session) / "takes" / check_id("take", take)


def take_json(take: Path) -> Path:
    return take / "take.json"


def report_json(take: Path) -> Path:
    return take / "report.json"


def closed_json(take: Path) -> Path:
    return take / "closed.json"


def raw_dir(take: Path) -> Path:
    return take / "raw"


def prep_dir(take: Path) -> Path:
    return take / "prep"


def extract_dir(take: Path) -> Path:
    return take / "extract"


def adapt_dir(take: Path) -> Path:
    return take / "adapt"


def blender_dir(take: Path) -> Path:
    return take / "blender"


def raw_video(take: Path, role: str) -> Path:
    return raw_dir(take) / f"{check_id('role', role)}.mkv"


def raw_timestamps(take: Path, role: str) -> Path:
    return raw_dir(take) / f"{check_id('role', role)}.timestamps.csv"


def prep_video(take: Path, role: str) -> Path:
    return prep_dir(take) / f"{check_id('role', role)}.mkv"


def synced_video(take: Path, role: str) -> Path:
    return extract_dir(take) / "synced" / f"{check_id('role', role)}.mp4"


def index_json(take: Path) -> Path:
    return extract_dir(take) / "index.json"


def quality_json(take: Path) -> Path:
    return extract_dir(take) / "quality.json"


def quality_md(take: Path) -> Path:
    return extract_dir(take) / "quality.md"


def mocap_take_json(take: Path) -> Path:
    return adapt_dir(take) / "mocap_take.json"


# ---------------------------------------------------------------- hand-off

def ready_sidecar(path: Path) -> Path:
    """Where the CameraFileReady event for `path` is written: next to it."""
    return path.with_name(path.name + ".ready.json")
