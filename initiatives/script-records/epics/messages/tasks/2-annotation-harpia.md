## 2. annotation.harpia and its catalog (owner: mocap-writer)

- **Depends on:** 1
- **Contract:**
  - Requires: `Annotation` (`annotations/<id>.json`): `id`
    (`annotation-<space>-<n>`), `kind` (`AnnotationKind`: note,
    character direction, prop direction, special effect, set direction,
    sound direction, general direction, transition, shot), `anchor`
    (`scene`, `element` index in the scene, the heading being 0, `quote`
    and its `occurrence`, none for a whole element), `text`, `by`,
    `shot` (the shot's number in its scene, shots only), `values`
    (`BibleValue`s checked against the annotation catalog);
    `ShotCounters` (`annotations/shot-counters.json`, the next shot
    number per scene); `AnnotationCatalog` (per kind its groups, as the
    bible's catalog), shipped as `catalog/annotation-v1.json` from the
    approved "Scene annotations" fields
  - Delivers: the messages, the catalog, `mocap_contracts.annotation`,
    fixtures `fixtures/annotation-v1/`
- **Tests:** fixtures; unknown field per kind refused; a shot without its
  number refused, a number on another kind refused
