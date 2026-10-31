## 1. workflow.harpia (owner: mocap-preprod, reviews: mocap-writer)

- **Depends on:** `v0.7.0`
- **Contract:**
  - Requires: three table messages.
    - `Proposal`: `id` (`proposal-<space>-<n>`, the agent's space),
      `item` (an existing bible record id), `value` (a `BibleValue`: state
      `proposal`, `by` the agent's name, `source` the memo's path relative
      to the film root), `time` (UTC, ISO 8601 with a Z), optional
      `change_set` (the `bible/sync/` file name the run answered).
    - `Review`: `proposal` (its id), `outcome` (`approved`, `rejected`,
      `edited`), `by` (`creator`), `time`, optional `note`, optional
      `text` (the creator's value when edited).
    - `Request`: `id` (`request-<space>-<n>`), `from` (an agent),
      `to` (an agent or `creator`), `items` (record ids), `scenes` (scene
      numbers), `what` (text), `source` (memo path), `time`, `status`
      (`open`, `done`, `declined`), optional `answer`, optional
      `answered_by`.
  - New record kind `RECORD_KIND_REQUEST` in `film.harpia`.
  - Rules: a proposal's value is checked against the catalog field of its
    item's map like any bible value, and its state is `proposal`, never
    `creator-approved`; ids of the right kind; at most one review per
    proposal; `text` only on `edited`; a request goes to someone other
    than its sender, has `what`, and `answer` only when not `open`.
  - Delivers: the messages, `fixtures/workflow-v1/` (one of each, JSON),
    invalid fixtures with `invalid/expected.json`
- **Tests:** fixtures round-trip byte for byte; each invalid one refused
  naming its field
