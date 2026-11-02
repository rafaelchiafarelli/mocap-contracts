"""script-records messages/1: script_settings.harpia and its rules."""

import json
from pathlib import Path

import pytest

import mocap_contracts as mc
from mocap_contracts import ContractError, from_json, to_json

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "script-v1"
EXPECTED = json.loads((FIXTURES / "invalid" / "expected.json").read_text())


def test_defaults_round_trip_byte_for_byte():
    text = (FIXTURES / "settings" / "script-settings.json").read_text()
    assert to_json(from_json(mc.ScriptSettings, text)) == text


def test_every_invalid_fixture_is_listed():
    files = {p.name for p in (FIXTURES / "invalid").glob("*.json")} - {"expected.json"}
    assert files == set(EXPECTED)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_invalid_fixture_is_refused_naming_its_field(name):
    case = EXPECTED[name]
    with pytest.raises(ContractError) as e:
        from_json(getattr(mc, case["message"]), (FIXTURES / "invalid" / name).read_text())
    assert case["error"] in str(e.value)


def test_strings_are_unicode():
    s = from_json(mc.ScriptSettings, (FIXTURES / "settings" / "script-settings.json").read_text())
    s.strings.dialogue_continued = " (continuação)"
    s.spelling_words.append("açúcar")
    assert from_json(mc.ScriptSettings, to_json(s)).spelling_words == ["açúcar"]


def test_a_title_page_layout():
    s = from_json(mc.ScriptSettings, (FIXTURES / "settings" / "script-settings.json").read_text())
    page = s.title_page.pages.add()
    page.strings.add(items=["A FILM"], x_mm=105.0, y_mm=70.5, size_pt=24,
                     align=mc.TextAlign.Value("TEXT_ALIGN_CENTER"), bold=2, italic=1, underlined=1,
                     font=mc.TitleFont.Value("TITLE_FONT_COURIER"))
    assert from_json(mc.ScriptSettings, to_json(s)).title_page.pages[0].strings[0].y_mm == 70.5
    page.strings[0].size_pt = 300
    with pytest.raises(ContractError, match="size_pt must be 4..288"):
        to_json(s)
