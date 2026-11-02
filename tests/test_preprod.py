"""preprod-records messages/1-3: scene_index, change_set, front_matter."""

import json
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "preprod-v1"
EXPECTED = json.loads((FIXTURES / "invalid" / "expected.json").read_text())
VALID = [("SceneIndex", "bible/scene-index.json"), ("ChangeSet", "bible/sync/changes.json"),
         ("FrontMatter", "settings/front-matter.json")]


@pytest.mark.parametrize("message, rel", VALID)
def test_valid_fixture_round_trips_byte_for_byte(message, rel):
    text = (FIXTURES / rel).read_text()
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


def test_an_unknown_name_has_no_id_and_names_keep_accents():
    s = from_json(mc.SceneIndex, (FIXTURES / "bible" / "scene-index.json").read_text())
    s.scenes[1].characters[0].name = "Bia Conceição"
    back = from_json(mc.SceneIndex, to_json(s))
    assert back.scenes[1].characters[0].name == "Bia Conceição"
    assert not back.scenes[1].characters[0].HasField("id")


def test_a_first_sync_has_no_from_hash_and_every_type_is_there():
    c = from_json(mc.ChangeSet, (FIXTURES / "bible" / "sync" / "changes.json").read_text())
    names = {mc.SceneChangeType.Name(x.type) for x in c.changes}
    assert names == set(mc.SceneChangeType.keys()) - {"SCENE_CHANGE_TYPE_UNSET"}
    c.ClearField("from_hash")
    assert not from_json(mc.ChangeSet, to_json(c)).HasField("from_hash")


def test_a_film_with_the_front_matter_and_source_parts():
    root = Path(__file__).resolve().parents[1] / "fixtures" / "film-v1"
    f = from_json(mc.Film, (root / "film.json").read_text())
    f.parts.add(name="front-matter", path="settings/front-matter.json", owner="writer")
    f.parts.add(name="source", path="source/", owner="writer")
    assert from_json(mc.Film, to_json(f)).parts[-1].name == "source"
