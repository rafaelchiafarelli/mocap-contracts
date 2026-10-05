import re

import mocap_contracts
from mocap_contracts import messages

HASH = re.compile(r"[0-9a-f]{32}")


def test_every_message_is_exported_without_a_hash():
    assert messages.__all__
    for name in messages.__all__:
        assert not HASH.search(name), name
        assert getattr(mocap_contracts, name) is getattr(messages, name)


def test_placeholder_round_trips_on_the_wire():
    msg = mocap_contracts.contracts_placeholder(note="hello")
    back = mocap_contracts.contracts_placeholder.FromString(msg.SerializeToString())
    assert back.note == "hello"
