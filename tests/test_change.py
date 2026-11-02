"""film-records messages/3: change.harpia, the change log of a film root."""

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, film, from_json, to_json
from samples import change


def _op(name):
    return mc.ChangeOp.Value(f"CHANGE_OP_{name}")


@pytest.mark.parametrize("op, before, after", [
    ("CREATE", None, "{}\n"), ("UPDATE", "{}\n", "{ }\n"), ("DELETE", "{}\n", None),
])
def test_each_op_round_trips(op, before, after):
    msg = change(op=_op(op), before=before, after=after)
    assert from_json(mc.Change, to_json(msg)) == msg


@pytest.mark.parametrize("op, before, after", [
    ("CREATE", "{}\n", "{}\n"), ("UPDATE", None, "{}\n"), ("UPDATE", "{}\n", None), ("DELETE", None, None),
])
def test_wrong_before_after_refused(op, before, after):
    with pytest.raises(ContractError, match=f"a {op.lower()} has"):
        to_json(change(op=_op(op), before=before, after=after))


@pytest.mark.parametrize("time", ["2026-10-28 14:03:12Z", "2026-10-28T14:03:12", "2026-02-30T00:00:00Z", ""])
def test_bad_time_refused(time):
    with pytest.raises(ContractError, match="time"):
        to_json(change(time=time))


def test_bad_path_and_record_refused():
    with pytest.raises(ContractError, match="path"):
        to_json(change(path="../x.json"))
    with pytest.raises(ContractError, match="record"):
        to_json(change(record="scene-w-1"))


def test_a_change_without_record():
    assert to_json(change(record=None, path="bible/not-props.json"))


def test_history_file():
    assert film.history_file("2026-10-28T14:03:12Z") == "history/2026-10.jsonl"
