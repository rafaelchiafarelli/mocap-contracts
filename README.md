# mocap-contracts

Data contracts shared by the Mocap Studio repositories: the `.harpia`
messages, the Python package generated from them (`mocap_contracts`) and the
session folder layout. Repositories talk to each other only through this
package and the folder layout.

## Layout

| Path | What | Edit? |
|---|---|---|
| `schema/mocap.harpia` | root file: imports only | yes |
| `schema/Include/*.harpia` | one module per owner repository | yes |
| `schema/project.harpia.yaml` | Harpia compliance profile (closed studio LAN) | rarely |
| `schema/schema_registry/` | frozen wire numbers, written by Harpia | **never delete**; commit |
| `gen/python/` | Harpia's generated Python project | no, regenerate |
| `mocap_contracts/messages.py` | re-exports every message under its declared name | no, regenerate |
| `third_party/harpia/` | Harpia, pinned to `V4` (black box) | no |

## Use

```python
import mocap_contracts
msg = mocap_contracts.ControlMenuOption(value=1, name="Manual Mode")
text = mocap_contracts.to_json(msg)          # declared fields only, defaults included
back = mocap_contracts.from_json(mocap_contracts.ControlMenuOption, text)
```

`from_json` raises `ContractError` on invalid JSON, on any key not declared in
`schema/` (Harpia's own `ID_/STATUS_/ERROR_<hash>` and `ORIGINATOR` fields
included), and on a missing `required` field at any nesting level. A `required` enum
holding its `*_UNSET` zero value counts as missing, and `to_json` refuses to
write what `from_json` would refuse to read.

Import from `mocap_contracts` only, never from `harpia_generated`. Its module
names carry a hash of the root `.harpia` and change with it.

## Develop

```bash
git submodule update --init          # Harpia, only needed to regenerate
python3.12 -m venv .venv
.venv/bin/pip install -e '.[test]'
make gen                             # after editing schema/ (needs Docker)
make test                            # full suite; the regeneration check is skipped without Docker
make check-gen                       # regenerate and fail on any diff
```

Writing `.harpia` (what Harpia's lexer accepts, beyond USAGE §3):
- comments: plain words only (`:` and similar punctuation are rejected)
- scalars: `int` (int32), `int64`, `float` (32-bit), `string`; there's no
  bool (use the `Flag` enum from `common.harpia`) and no double
- enums: one value per line; every enum's zero value is `<ENUM>_UNSET`, and
  every value is prefixed with its enum's name

Plan and progress: `initiatives/`.
