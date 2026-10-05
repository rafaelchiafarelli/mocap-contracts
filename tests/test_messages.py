import re

import mocap_contracts
from mocap_contracts import messages

HASH = re.compile(r"[0-9a-f]{32}")


def test_every_message_is_exported_without_a_hash():
    assert messages.__all__
    for name in messages.__all__:
        assert not HASH.search(name), name
        assert getattr(mocap_contracts, name) is getattr(messages, name)


def test_every_contract_enum_has_unset_as_zero():
    enums = [n for n in messages.__all__ if n not in messages.DECLARED_FIELDS]
    assert enums
    for name in enums:
        zero = getattr(mocap_contracts, name).DESCRIPTOR.values_by_number[0].name
        assert zero.endswith("_UNSET"), (name, zero)


def test_a_message_round_trips_on_the_wire():
    msg = mocap_contracts.ControlMenuOption(value=3, name="aperture_priority")
    back = mocap_contracts.ControlMenuOption.FromString(msg.SerializeToString())
    assert (back.value, back.name) == (3, "aperture_priority")
