"""workflow-records workflow/1: workflow.harpia (Proposal, Review, Request) and its rules."""

import json
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "workflow-v1"
EXPECTED = json.loads((FIXTURES / "invalid" / "expected.json").read_text())
VALID = [("Proposal", "proposal.json"), ("Review", "review.json"), ("Request", "request.json")]


@pytest.mark.parametrize("message,name", VALID)
def test_valid_fixtures_round_trip_byte_for_byte(message, name):
    text = (FIXTURES / name).read_text()
    assert to_json(from_json(getattr(mc, message), text)) == text


def test_every_invalid_fixture_is_listed():
    files = {p.name for p in (FIXTURES / "invalid").glob("*.json")} - {"expected.json"}
    assert files == set(EXPECTED)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_invalid_fixture_is_refused_naming_its_field(name):
    case = EXPECTED[name]
    with pytest.raises(ContractError) as e:
        from_json(getattr(mc, case["message"]), (FIXTURES / "invalid" / name).read_text())
    assert case["error"] in str(e.value)


def test_request_is_a_record_kind():
    assert "request" in mc.film.KINDS
    assert mc.film.record_id("request", "pcp", 3) == "request-pcp-3"


def test_the_proposal_kind_keeps_its_wire_number():
    assert mc.RecordKind.Value("RECORD_KIND_PROPOSAL") == 6
    assert mc.RecordKind.Value("RECORD_KIND_REQUEST") == 7


def _request(**kw):
    r = from_json(mc.Request, (FIXTURES / "request.json").read_text())
    for k, v in kw.items():
        r.ClearField(k) if v is None else setattr(r, k, v)
    return r


def test_an_open_request_has_no_answer():
    r = _request(status=mc.RequestStatus.Value("REQUEST_STATUS_OPEN"), answer=None, answered_by=None)
    assert from_json(mc.Request, to_json(r)) == r


def test_a_request_can_go_to_another_agent():
    r = _request(to="sound-design-planner")
    assert from_json(mc.Request, to_json(r)).to == "sound-design-planner"


def test_a_request_to_the_writer_is_refused():
    with pytest.raises(ContractError, match="to must be an agent name"):
        to_json(_request(to="writer"))


def test_a_rejected_review_has_no_text():
    r = from_json(mc.Review, (FIXTURES / "review.json").read_text())
    r.outcome = mc.ReviewOutcome.Value("REVIEW_OUTCOME_REJECTED")
    r.ClearField("text")
    assert from_json(mc.Review, to_json(r)) == r
    r.outcome = mc.ReviewOutcome.Value("REVIEW_OUTCOME_EDITED")
    with pytest.raises(ContractError, match="only an edited one, has text"):
        to_json(r)


def test_a_proposal_number_needs_its_unit():
    p = from_json(mc.Proposal, (FIXTURES / "proposal.json").read_text())
    p.value.field = "look.height"
    p.value.ClearField("text")
    p.value.number = "12.5"
    with pytest.raises(ContractError, match="a number has a unit"):
        to_json(p)
    p.value.unit = "cm"
    assert from_json(mc.Proposal, to_json(p)).value.number == "12.5"
