"""Build fixtures/workflow-v1/ (workflow.harpia test fixtures).

Run once; the outputs are committed. Stdlib only, so the fixtures don't come
from the code they test.

    python3 tools/make_workflow_fixtures.py

Writes one record of each table of the film's workflow database as JSON: an
agent's proposal for a prop of fixtures/bible-v1/, the creator's edited
review of it, a request from that agent to the creator answered; and
invalid ones with invalid/expected.json.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "fixtures" / "workflow-v1"

AGENT = "props-continuity-planner"
MEMO = "analysis/props-continuity.md"

PROPOSAL = {
    "id": "proposal-pcp-1",
    "item": "prop-pcp-1",
    "value": {
        "field": "look.shape",
        "text": "tall, with a narrow handle",
        "state": "VALUE_STATE_PROPOSAL",
        "source": MEMO,
        "department": "props",
        "by": AGENT,
    },
    "time": "2026-10-31T12:00:00Z",
    "change_set": "2026-10-31T11-00-00Z-changes.json",
}
REVIEW = {
    "proposal": "proposal-pcp-1",
    "outcome": "REVIEW_OUTCOME_EDITED",
    "by": "creator",
    "time": "2026-10-31T13:00:00Z",
    "note": "Shorter, it has to fit the shelf.",
    "text": "short, with a narrow handle",
}
REQUEST = {
    "id": "request-pcp-1",
    "from": AGENT,
    "to": "creator",
    "items": ["prop-pcp-1", "character-w-1"],
    "scenes": ["1", "2"],
    "what": "Who keeps the cup between scenes 1 and 2?",
    "source": MEMO,
    "time": "2026-10-31T12:05:00Z",
    "status": "REQUEST_STATUS_DONE",
    "answer": "Ana takes it with her.",
    "answered_by": "creator",
}
VALID = {"proposal.json": PROPOSAL, "review.json": REVIEW, "request.json": REQUEST}


def _bad(base, edit):
    data = copy.deepcopy(base)
    edit(data)
    return data


INVALID = {
    "proposal-approved": ("Proposal", _bad(PROPOSAL, lambda d: d["value"].update(
        state="VALUE_STATE_CREATOR_APPROVED")), "Proposal: value: state must be VALUE_STATE_PROPOSAL"),
    "proposal-bad-id": ("Proposal", _bad(PROPOSAL, lambda d: d.update(id="request-pcp-1")),
                        "Proposal: id must be a proposal id"),
    "proposal-unknown-field": ("Proposal", _bad(PROPOSAL, lambda d: d["value"].update(
        field="look.mood")), "Proposal: value: 'look.mood' is not a prop field of the catalog"),
    "proposal-not-an-item": ("Proposal", _bad(PROPOSAL, lambda d: d.update(item="annotation-w-1")),
                             "Proposal: item must be a record id of a map"),
    "proposal-by-creator": ("Proposal", _bad(PROPOSAL, lambda d: d["value"].update(by="creator")),
                            "Proposal: value: by must be an agent name"),
    "proposal-source-absolute": ("Proposal", _bad(PROPOSAL, lambda d: d["value"].update(
        source="/home/analysis/props.md")), "Proposal: value: source is the memo's film path"),
    "proposal-change-set-path": ("Proposal", _bad(PROPOSAL, lambda d: d.update(
        change_set="bible/sync/2026-10-31T11-00-00Z-changes.json")),
        "Proposal: change_set is a bible/sync/ file name"),
    "proposal-bad-time": ("Proposal", _bad(PROPOSAL, lambda d: d.update(time="2026-10-31 12:00")),
                          "Proposal: time must be UTC ISO-8601"),
    "review-not-creator": ("Review", _bad(REVIEW, lambda d: d.update(by="writer")),
                           "Review: by must be 'creator'"),
    "review-text-not-edited": ("Review", _bad(REVIEW, lambda d: d.update(
        outcome="REVIEW_OUTCOME_APPROVED")), "Review: an edited review, and only an edited one, has text"),
    "review-bad-proposal": ("Review", _bad(REVIEW, lambda d: d.update(proposal="prop-pcp-1")),
                            "Review: id must be a proposal id"),
    "request-to-itself": ("Request", _bad(REQUEST, lambda d: d.update(to=AGENT)),
                          "Request: to can't be the sender"),
    "request-from-creator": ("Request", _bad(REQUEST, lambda d: d.update(**{"from": "creator"})),
                             "Request: from must be an agent name"),
    "request-no-what": ("Request", _bad(REQUEST, lambda d: d.update(what=" ")),
                        "Request: what is empty"),
    "request-open-answered": ("Request", _bad(REQUEST, lambda d: d.update(
        status="REQUEST_STATUS_OPEN")), "Request: an open request has no answer or answered_by"),
    "request-bad-scene": ("Request", _bad(REQUEST, lambda d: d.update(scenes=["1a"])),
                          "Request: scenes must be scene numbers"),
    "request-bad-item": ("Request", _bad(REQUEST, lambda d: d.update(items=["cup"])),
                         "Request: items must be record ids"),
}


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    for name, data in VALID.items():
        _write(OUT / name, data)
    expected = {}
    for name, (message, data, error) in INVALID.items():
        _write(OUT / "invalid" / f"{name}.json", data)
        expected[f"{name}.json"] = {"message": message, "error": error}
    _write(OUT / "invalid" / "expected.json", expected)


if __name__ == "__main__":
    main()
