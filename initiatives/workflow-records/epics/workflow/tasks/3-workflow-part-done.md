## 3. The film part `workflow`

- **Depends on:** 2
- **Contract:** part name `workflow`, default path `workflow.sqlite`,
  owner `shared`; `shared` is accepted as an owner only for this part.
  Ownership inside it is per table: proposals and requests are written by
  the agent whose space they carry, reviews by the writer; answering a
  request by its recipient. Documented in `film.harpia`'s comments and in
  the rules.
- **Tests:** a `film.json` with the part reads; `shared` on another part
  refused; the fixture film index updated
