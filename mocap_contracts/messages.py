"""Every contract message and enum, under its declared name.

Written by tools/harpia_gen.py (`make gen`); do not edit. Harpia's
module names carry a hash of the root .harpia file and change with it;
import from here (or from mocap_contracts) instead."""

from harpia_generated.protofiles.contracts_placeholder_fb15c485dc8666ed616f54252a0db38b_pb2 import contracts_placeholder

# Field names as declared in schema/ (Harpia's bookkeeping fields excluded).
DECLARED_FIELDS: dict[str, tuple[str, ...]] = {
    'contracts_placeholder': ('note',),
}

# Fields declared `required` (proto3 doesn't keep it).
REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    'contracts_placeholder': ('note',),
}

__all__ = [
    "contracts_placeholder",
]
