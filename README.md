# mocap-contracts

Data contracts shared by the Mocap Studio repositories: the `.harpia`
messages, the Python package generated from them (`mocap_contracts`) and the
session folder layout. Repositories talk to each other only through this
package and the folder layout.

## Develop

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e '.[test]'
.venv/bin/pytest
```

Plan and progress: `initiatives/`.
