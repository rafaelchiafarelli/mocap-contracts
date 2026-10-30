"""script-records messages/2: annotation.harpia, its catalog and rules."""

import json
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, annotation, from_json, to_json

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "annotation-v1"
EXPECTED = json.loads((FIXTURES / "invalid" / "expected.json").read_text())
VALID = sorted(p.name for p in FIXTURES.glob("annotation-*.json"))

# the kinds of mocap-writer film-bible contract/1, "Scene annotations"
KINDS = ("note", "character_direction", "prop_direction", "special_effect", "set_direction",
         "sound_direction", "general_direction", "transition", "shot")


def test_kinds_come_from_the_schema():
    assert annotation.KINDS == KINDS


def test_catalog_round_trips_and_has_every_kind():
    text = annotation.CATALOG_FILE.read_text(encoding="utf-8")
    cat = from_json(mc.AnnotationCatalog, text)
    assert to_json(cat) == text
    assert [annotation.kind_word(k.kind) for k in cat.kinds] == list(KINDS)


def test_shot_fields():
    groups = {f.group for f in annotation.fields("shot").values()}
    assert groups == {"framing", "lens", "movement", "timing", "lighting", "previz", "general"}


@pytest.mark.parametrize("name", VALID + ["shot-counters.json"])
def test_valid_fixtures_round_trip_byte_for_byte(name):
    cls = mc.ShotCounters if name == "shot-counters.json" else mc.Annotation
    text = (FIXTURES / name).read_text()
    assert to_json(from_json(cls, text)) == text


def test_every_invalid_fixture_is_listed():
    files = {p.name for p in (FIXTURES / "invalid").glob("*.json")} - {"expected.json"}
    assert files == set(EXPECTED)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_invalid_fixture_is_refused_naming_its_field(name):
    case = EXPECTED[name]
    with pytest.raises(ContractError) as e:
        from_json(getattr(mc, case["message"]), (FIXTURES / "invalid" / name).read_text())
    assert case["error"] in str(e.value)


def test_shot_names():
    assert annotation.shot_name("12.A", 4) == "12.A S4"
    assert annotation.shot_file_name("12.A", 4) == "12.A_S4"
    assert mc.film.path_problem(annotation.shot_file_name("12.A", 4)) is None


def test_an_annotation_id_is_a_record_id():
    assert mc.film.check_record_id("annotation-w-12")
