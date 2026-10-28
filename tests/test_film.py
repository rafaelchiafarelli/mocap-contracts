"""film-root film-messages/1: film.harpia, its rules and the record ids."""

import json
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, film, from_json, to_json
from samples import film as sample_film
from samples import id_counters

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "film-v1"
EXPECTED = json.loads((FIXTURES / "invalid" / "expected.json").read_text())

# The regex as written in mocap-writer file-format/layout/1 (Rafael, 2026-10-26).
LAYOUT_1_REGEX = r"^(set|character|prop|wardrobe|annotation|proposal)-[a-z][a-z0-9]{0,7}-[1-9][0-9]*$"


@pytest.mark.parametrize("rel, cls", [
    ("film.json", mc.Film), ("ids/w.json", mc.IdCounters), ("ids/pcp.json", mc.IdCounters),
])
def test_valid_fixtures_round_trip_byte_for_byte(rel, cls):
    text = (FIXTURES / rel).read_text()
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


def test_invalid_film_is_never_written():
    with pytest.raises(ContractError, match="format_version"):
        to_json(sample_film(format_version=0))


def test_folder_parts_with_a_shared_prefix_are_apart():
    parts = [p for p in sample_film().parts if p.name != "history"]
    parts.append(mc.FilmPart(name="history", path="bible-old/", owner="writer"))
    assert from_json(mc.Film, to_json(sample_film(parts=parts))).parts[-1].path == "bible-old/"


def test_same_path_twice_is_refused():
    parts = [p for p in sample_film().parts if p.name != "history"]
    parts.append(mc.FilmPart(name="history", path="bible", owner="writer"))
    with pytest.raises(ContractError, match="'bible' and 'history'"):
        to_json(sample_film(parts=parts))


def test_film_json_is_not_a_part():
    with pytest.raises(ContractError, match=r"Film.parts\[0\]: path can't be film.json"):
        to_json(sample_film(parts=[mc.FilmPart(name="script", path="film.json", owner="writer")]))


def test_counters_are_written_in_key_order():
    assert list(json.loads(to_json(id_counters(set=1, character=2, prop=3)))["next"]) == [
        "character", "prop", "set"]


def test_a_new_space_has_no_counters_yet():
    assert to_json(mc.IdCounters()) == '{\n  "next": {}\n}\n'


# ---------------------------------------------------------------- ids

def test_kinds_come_from_the_schema():
    assert film.KINDS == ("set", "character", "prop", "wardrobe", "annotation", "proposal")


def test_record_id_regex_is_the_layout_1_one():
    assert film.RECORD_ID.pattern == LAYOUT_1_REGEX


@pytest.mark.parametrize("value", ["character-w-1", "prop-pcp-3", "proposal-w2-120", "set-abcdefgh-9"])
def test_valid_record_ids(value):
    assert film.check_record_id(value) == value


@pytest.mark.parametrize("value", [
    "character-w-0", "character-w-012", "scene-w-1", "Character-w-1", "character-W-1",
    "character-2w-1", "character-abcdefghi-1", "character_w_1", "character-w-1 ", "character--1",
])
def test_invalid_record_ids(value):
    with pytest.raises(ContractError):
        film.check_record_id(value)


def test_record_id_builds_the_form():
    assert film.record_id("character", "w", 12) == "character-w-12"
    assert film.check_record_id(film.record_id("prop", "pcp", 3))


@pytest.mark.parametrize("args", [("scene", "w", 1), ("prop", "W", 1), ("prop", "w", 0),
                                  ("prop", "w", True), ("prop", "w", "1")])
def test_record_id_refuses_bad_parts(args):
    with pytest.raises(ContractError):
        film.record_id(*args)


def test_two_spaces_never_collide():
    w = {film.record_id(k, "w", n) for k in film.KINDS for n in range(1, 50)}
    w2 = {film.record_id(k, "w2", n) for k in film.KINDS for n in range(1, 50)}
    assert not w & w2


def test_root_files():
    assert film.FILM_FILE == "film.json"
    assert film.ids_file("pcp") == "ids/pcp.json"
    with pytest.raises(ContractError):
        film.ids_file("../x")


@pytest.mark.parametrize("value", [
    "script.fountain", "bible/", "bible/props/xicara-azul/item.json", "photos/Foto 1.jpg",
])
def test_film_paths(value):
    assert film.check_path(value) == value


@pytest.mark.parametrize("value", [
    "", "/abs", "a\\b", "C:/x", "a//b", "../x", "a/./b", "x?.json", "a|b", "dot./x", "space /x",
    "CON", "nul.txt", "a/COM1.json", "tab\there",
])
def test_bad_film_paths(value):
    with pytest.raises(ContractError):
        film.check_path(value)


def test_owner_form():
    assert film.OWNER.fullmatch("props-continuity-planner")
    assert not film.OWNER.fullmatch("Props") and not film.OWNER.fullmatch("a--b")
