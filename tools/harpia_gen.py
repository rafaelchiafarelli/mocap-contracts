"""Generate the Python contracts from schema/ with Harpia (the `make gen` step).

Harpia is used as a black box, as its USAGE.md (V4, §5.1-5.4) documents:
the input folder is staged under the Harpia repo (Docker mounts it at
/harpia), `main.py` runs with HARPIA_GEN_LANG=python, and then:

- schema_registry/ (frozen wire numbers) is copied back into schema/,
- the generated python/ project replaces gen/python/,
- mocap_contracts/messages.py is rewritten to re-export every message and
  enum under its declared name, so consumers never see the <hash> in
  Harpia's module names.

Stdlib only. Usage: python3 tools/harpia_gen.py [--into DIR]
(--into writes the three outputs under DIR instead of the repo; the
reproducibility test uses it.)
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema"
HARPIA = ROOT / "third_party" / "harpia"
ROOT_FILE = "mocap.harpia"
HARPIA_STAGE = HARPIA / "build" / "mocap-contracts"  # Harpia's .gitignore covers build/

GEN_PYTHON = Path("gen") / "python"
MESSAGES_PY = Path("mocap_contracts") / "messages.py"
REGISTRY = Path("schema") / "schema_registry"

# a user module's .proto: <name>_<32 hex>.proto (not the _service companion)
USER_PROTO = re.compile(r"^(?P<stem>.+_(?P<hash>[0-9a-f]{32}))\.proto$")
TOP_LEVEL = re.compile(r"^(message|enum)\s+(\w+)\s*\{")


def run_harpia(stage: Path) -> Path:
    """Stage schema/ under the Harpia mount, generate, return the output dir."""
    if stage.exists():
        shutil.rmtree(stage)
    inp, out = stage / "in", stage / "out"
    shutil.copytree(SCHEMA, inp)
    rel = inp.relative_to(HARPIA)
    cmd = [
        "Docker/run.sh", "env",
        "HARPIA_GEN_LANG=python",
        f"HARPIA_INPUT_FILE=./{rel}/{ROOT_FILE}",
        f"HARPIA_INCLUDE_FOLDER=./{rel}/Include",
        f"HARPIA_COMPLIANCE_CONFIG=./{rel}/project.harpia.yaml",
        f"HARPIA_OUTPUT_DIR=/harpia/{out.relative_to(HARPIA)}",
        "python3", "main.py",
    ]
    proc = subprocess.run(cmd, cwd=HARPIA, capture_output=True, text=True)
    if proc.returncode != 0 or not (out / "python").is_dir():
        sys.stderr.write(proc.stdout[-4000:] + proc.stderr[-4000:])
        raise SystemExit(f"harpia generation failed (exit {proc.returncode})")
    return out


def top_level_names(proto: Path) -> list[str]:
    names, depth = [], 0
    for line in proto.read_text().splitlines():
        if depth == 0 and (m := TOP_LEVEL.match(line.strip())):
            names.append(m.group(2))
        depth += line.count("{") - line.count("}")
    return names


def messages_module(python_dir: Path) -> str:
    protos = python_dir / "proto" / "harpia_generated" / "protofiles"
    lines = [
        '"""Every contract message and enum, under its declared name.',
        "",
        "Written by tools/harpia_gen.py (`make gen`); do not edit. Harpia's",
        "module names carry a hash of the root .harpia file and change with it;",
        'import from here (or from mocap_contracts) instead."""',
        "",
    ]
    exported: list[str] = []
    for proto in sorted(protos.glob("*.proto")):
        m = USER_PROTO.match(proto.name)
        if not m:
            continue
        names = top_level_names(proto)
        if names:
            lines.append(
                f"from harpia_generated.protofiles.{m['stem']}_pb2 import "
                + ", ".join(names)
            )
            exported += names
    if not exported:
        raise SystemExit("no messages found in the generated .proto files")
    lines += ["", "__all__ = ["] + [f'    "{n}",' for n in sorted(exported)] + ["]", ""]
    return "\n".join(lines)


def write_outputs(out: Path, into: Path) -> None:
    gen_python = into / GEN_PYTHON
    if gen_python.exists():
        shutil.rmtree(gen_python)
    shutil.copytree(out / "python", gen_python,
                    ignore=shutil.ignore_patterns("__pycache__"))

    registry_src = HARPIA_STAGE / "in" / "schema_registry"
    registry = into / REGISTRY
    if registry.exists():
        shutil.rmtree(registry)
    shutil.copytree(registry_src, registry)

    (into / MESSAGES_PY).parent.mkdir(parents=True, exist_ok=True)
    (into / MESSAGES_PY).write_text(messages_module(out / "python"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--into", type=Path, default=ROOT,
                    help="where to write gen/python, schema/schema_registry "
                         "and mocap_contracts/messages.py (default: the repo)")
    args = ap.parse_args()
    if not (HARPIA / "Docker" / "run.sh").exists():
        raise SystemExit("third_party/harpia is missing: git submodule update --init")
    out = run_harpia(HARPIA_STAGE)
    write_outputs(out, args.into.resolve())


if __name__ == "__main__":
    main()
