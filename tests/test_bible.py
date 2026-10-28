"""film-records messages/2: bible.harpia, the catalog and its rules."""

import json
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, bible, from_json, to_json

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "bible-v1"
EXPECTED = json.loads((FIXTURES / "invalid" / "expected.json").read_text())
ITEMS = sorted(p.relative_to(FIXTURES).as_posix() for p in FIXTURES.rglob("item.json")
               if "invalid" not in p.parts)

# Every group of mocap-writer film-bible contract/1 (approved 2026-10-26).
CONTRACT_1 = {
    "set": ["general", "space", "size", "openings", "surfaces", "style", "light", "sound",
            "senses", "dressing", "continuity", "capture", "realization", "connections", "safety"],
    "character": ["general", "identity", "inner_life", "body", "face", "hair", "hands", "voice",
                  "behavior", "relationships", "capture", "per_scene"],
    "prop": ["general", "identity", "look", "touch", "senses", "behavior", "handling", "state",
             "capture", "realization", "ownership"],
    "wardrobe": ["general", "piece", "condition", "meaning", "behavior", "files", "changes",
                 "capture", "realization", "hair_makeup"],
}


def test_catalog_round_trips_byte_for_byte():
    text = bible.CATALOG_FILE.read_text(encoding="utf-8")
    assert to_json(from_json(mc.BibleCatalog, text)) == text


def test_catalog_holds_every_group_of_contract_1():
    groups = {bible.map_word(m.bible_map): [g.key for g in m.groups] for m in bible.catalog().maps}
    assert groups == CONTRACT_1


@pytest.mark.parametrize("map_, folder", bible.MAP_FOLDERS.items())
def test_maps_are_record_kinds(map_, folder):
    assert map_ in mc.film.KINDS and folder in ("sets", "characters", "props", "wardrobe")


def test_per_scene_groups():
    per_scene = {f.group for m in bible.MAPS for f in bible.fields(m).values() if f.per_scene}
    assert per_scene == {"continuity", "per_scene", "state", "changes", "hair_makeup"}


@pytest.mark.parametrize("rel", ITEMS)
def test_valid_items_round_trip_byte_for_byte(rel):
    text = (FIXTURES / rel).read_text()
    assert to_json(from_json(mc.BibleItem, text)) == text


def test_not_props_round_trips():
    text = (FIXTURES / "not-props.json").read_text()
    assert to_json(from_json(mc.NotProps, text)) == text


def test_every_invalid_fixture_is_listed():
    files = {p.name for p in (FIXTURES / "invalid").glob("*.json")} - {"expected.json"}
    assert files == set(EXPECTED)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_invalid_fixture_is_refused_naming_its_field(name):
    case = EXPECTED[name]
    with pytest.raises(ContractError) as e:
        from_json(getattr(mc, case["message"]), (FIXTURES / "invalid" / name).read_text())
    assert case["error"] in str(e.value)


def test_choice_takes_a_free_other():
    item = from_json(mc.BibleItem, (FIXTURES / "props/blue-cup/item.json").read_text())
    assert [v.text for v in item.values if v.field == "look.material"] == ["enamel"]


def test_list_file_and_link_fields_repeat():
    def tag(text):
        return mc.BibleValue(field="general.tags", text=text, state=mc.ValueState.Value("VALUE_STATE_TBD"),
                             source="1", department="props", by="writer", revisit="later")
    to_json(mc.BibleItem(id="prop-w-1", name="x", values=[tag("a"), tag("b")]))


@pytest.mark.parametrize("name, slug", [
    ("Xícara Azul", "xicara-azul"), ("  Sala de Jantar! ", "sala-de-jantar"), ("CAIXA E VELA", "caixa-e-vela"),
    ("???", "item"), ("Ação/Reação", "acao-reacao"),
])
def test_slug(name, slug):
    assert bible.slug(name) == slug
    assert mc.film.path_problem(slug) is None


@pytest.mark.parametrize("scene, ok", [
    ("12", True), ("12.A", True), ("12.A.1", True), ("12.A.1.B", True),
    ("0", False), ("12A", False), ("12.a", False), ("12.AB", False), ("12.A.0", False), ("", False),
])
def test_scene_numbers(scene, ok):
    assert bool(bible.SCENE.fullmatch(scene)) == ok


def test_map_of():
    assert bible.map_of("wardrobe-pcp-2") == "wardrobe"
    assert bible.map_of("annotation-w-1") is None
