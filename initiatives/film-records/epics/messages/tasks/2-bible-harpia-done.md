## 2. bible.harpia and the catalog (owner: mocap-writer)

- **Status:** Done (2026-10-28)

- **Depends on:** 1
- **Contract:**
  - In: the approved catalog (`mocap-writer` film-bible contract/1) and the
    decided shape (contract/2, 2026-10-28)
  - Requires:
    - enums `BibleMap` (`SET`, `CHARACTER`, `PROP`, `WARDROBE`),
      `FieldType` (`TEXT`, `NUMBER`, `CHOICE`, `LIST`, `FILE`, `LINK`),
      `ValueState` (`SCRIPT_STATED`, `CREATOR_APPROVED`, `PROPOSAL`, `TBD`);
    - `BibleCatalog` (`version`, `maps`) → `CatalogMap` (`map`, `groups`)
      → `CatalogGroup` (`key`, `label`, `per_scene` Flag, `fields`) →
      `CatalogField` (`key`, `label`, `type`, `options`, `unit`,
      `link_kind`); a field is named `<group>.<field>`;
    - `BibleItem` (`item.json`): `id` (a record id of kind set, character,
      prop or wardrobe), `name`, `aliases`, `parent` (optional, an id of
      the same kind), `values`, `links`;
    - `BibleValue`: `field`, `scene` (only and always in a per-scene
      group), one of `text` (text, choice, list, file, link) or `number` +
      `unit`, `state`, `source`, `department`, `by`, `revisit` (required
      when the state is `TBD`);
    - `BibleLink`: `scene` (scene number), `item` (wardrobe only: the
      character id who wears it there);
    - `NotProps` (`bible/not-props.json`): `words`.
  - Rules: a value's field is in the catalog of the item's map; its
    payload fits the type (a number is a decimal and has a unit; a link is
    a record id of the field's `link_kind`; a file is a relative path
    inside the item's folder, `check_path`; a choice may hold text outside
    its options, the free "other"); a field that is not a list, link or
    file appears once per scene key; `by` is `creator`, `writer` or an
    owner; scene numbers are in the writer's form (`12`, `12.A`,
    `12.A.1`); links are unique.
  - Delivers: `schema/Include/bible.harpia`; `mocap_contracts/catalog/bible-v1.json`
    (the approved catalog, read with `from_json(BibleCatalog)`);
    `mocap_contracts.bible` (`MAPS`, `catalog()`, `field(map, key)`,
    `SCENE`, `slug(name)`); fixtures `fixtures/bible-v1/` (one item per
    map, a child item, invalid items with `invalid/expected.json`)
- **Tests:** every fixture; the catalog holds every group of contract/1;
  unknown field, wrong type, missing unit, `TBD` without revisit, a link
  to the wrong kind, per-scene value without a scene are refused
