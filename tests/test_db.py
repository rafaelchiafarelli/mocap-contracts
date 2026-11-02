"""workflow-records workflow/2: mocap_contracts.db, the film's workflow database."""

import sqlite3
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, db, from_json

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "workflow-v1"
TABLES = [("proposals", "Proposal", "proposal.json", "proposal-pcp-1"),
          ("reviews", "Review", "review.json", "proposal-pcp-1"),
          ("requests", "Request", "request.json", "request-pcp-1")]


def _record(message, name):
    return from_json(getattr(mc, message), (FIXTURES / name).read_text())


@pytest.fixture
def path(tmp_path):
    return tmp_path / "workflow.sqlite"


@pytest.mark.parametrize("table,message,name,key", TABLES)
def test_create_read_list_each_table(path, table, message, name, key):
    record = _record(message, name)
    with db.open(path) as d:
        t = getattr(d, table)
        assert t.read(key) is None
        t.create(record)
        assert t.read(key) == record
        assert t.list() == [record]
        assert mc.to_json(t.read(key)) == (FIXTURES / name).read_text()


def test_update_each_table(path):
    with db.open(path) as d:
        p = _record("Proposal", "proposal.json")
        d.proposals.create(p)
        p.value.text = "squat"
        assert d.proposals.update(p)
        assert d.proposals.read(p.id).value.text == "squat"

        r = _record("Review", "review.json")
        d.reviews.create(r)
        r.note = "Keep the handle."
        assert d.reviews.update(r)
        assert d.reviews.read(r.proposal).note == "Keep the handle."

        q = _record("Request", "request.json")
        d.requests.create(q)
        del q.items[1:]
        q.scenes.append("3")
        assert d.requests.update(q)
        got = d.requests.read(q.id)
        assert list(got.items) == ["prop-pcp-1"] and list(got.scenes) == ["1", "2", "3"]
        assert len(d.requests.list()) == 1


def test_update_of_an_unknown_record_is_false(path):
    with db.open(path) as d:
        assert d.proposals.update(_record("Proposal", "proposal.json")) is False
        assert d.proposals.list() == []


def test_absent_optional_fields_stay_absent(path):
    p = _record("Proposal", "proposal.json")
    p.ClearField("change_set")
    r = _record("Review", "review.json")
    r.outcome = mc.ReviewOutcome.Value("REVIEW_OUTCOME_APPROVED")
    r.ClearField("note")
    r.ClearField("text")
    with db.open(path) as d:
        d.proposals.create(p)
        d.reviews.create(r)
        got = d.proposals.read(p.id)
        assert not got.HasField("change_set")
        assert not got.value.HasField("scene") and not got.value.HasField("number")
        assert not d.reviews.read(r.proposal).HasField("text")


def test_an_empty_note_stays_set(path):
    r = _record("Review", "review.json")
    r.note = ""
    with db.open(path) as d:
        d.reviews.create(r)
        assert d.reviews.read(r.proposal).HasField("note")


def test_create_keeps_the_callers_message_as_it_was(path):
    p = _record("Proposal", "proposal.json")
    before = p.SerializeToString(deterministic=True)
    with db.open(path) as d:
        d.proposals.create(p)
    assert p.SerializeToString(deterministic=True) == before


def test_invalid_record_is_refused_and_nothing_written(path):
    bad = _record("Proposal", "proposal.json")
    bad.value.state = mc.ValueState.Value("VALUE_STATE_CREATOR_APPROVED")
    with db.open(path) as d:
        with pytest.raises(ContractError, match="state must be VALUE_STATE_PROPOSAL"):
            d.proposals.create(bad)
        assert d.proposals.list() == []


def test_invalid_update_is_refused_and_the_record_kept(path):
    q = _record("Request", "request.json")
    with db.open(path) as d:
        d.requests.create(q)
        bad = _record("Request", "request.json")
        bad.to = getattr(bad, "from")
        with pytest.raises(ContractError, match="to can't be the sender"):
            d.requests.update(bad)
        assert d.requests.read(q.id) == q


def test_missing_required_field_is_refused(path):
    with db.open(path) as d:
        with pytest.raises(ContractError, match="required field"):
            d.requests.create(mc.Request(id="request-pcp-1"))
        assert d.requests.list() == []


def test_a_key_is_used_once(path):
    with db.open(path) as d:
        d.proposals.create(_record("Proposal", "proposal.json"))
        with pytest.raises(ContractError, match="proposal-pcp-1' already exists"):
            d.proposals.create(_record("Proposal", "proposal.json"))
        assert len(d.proposals.list()) == 1


def test_at_most_one_review_per_proposal(path):
    with db.open(path) as d:
        d.reviews.create(_record("Review", "review.json"))
        with pytest.raises(ContractError, match="already exists"):
            d.reviews.create(_record("Review", "review.json"))


def test_list_pages_in_the_order_made(path):
    with db.open(path) as d:
        for n in range(1, 6):
            p = _record("Proposal", "proposal.json")
            p.id = f"proposal-pcp-{n}"
            d.proposals.create(p)
        assert [p.id for p in d.proposals.list(1, 2)] == ["proposal-pcp-2", "proposal-pcp-3"]


def test_opens_again_after_a_no_op_migration(path):
    record = _record("Request", "request.json")
    with db.open(path) as d:
        d.requests.create(record)
    with db.open(path) as d:
        assert d.requests.list() == [record]


def test_version_stamped_and_rollback_journal(path):
    db.open(path).close()
    conn = sqlite3.connect(path)
    stamped = dict(conn.execute('SELECT "name", "version" FROM "_harpia_schema_version"'))
    assert set(stamped) == {"proposal_table", "review_table", "request_table"}
    assert conn.execute("PRAGMA journal_mode").fetchone()[0] == "delete"
    conn.close()
