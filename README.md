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
msg = mocap_contracts.contracts_placeholder(note="hi")
```

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

Comments in `.harpia` files: plain words only. Harpia's lexer rejects
punctuation such as `:` inside comments.

Plan and progress: `initiatives/`.
