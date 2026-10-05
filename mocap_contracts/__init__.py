"""Data contracts shared by the Mocap Studio repositories.

Messages are generated from the `.harpia` sources in schema/ by Harpia and
re-exported here under their declared names; consumers import from this
package only, never from the generated modules.
"""

from mocap_contracts.jsonio import ContractError, from_json, to_json
from mocap_contracts.messages import *  # noqa: F403
from mocap_contracts.messages import __all__ as _messages

__version__ = "0.0.1"
__all__ = ["__version__", "ContractError", "from_json", "to_json", *_messages]
