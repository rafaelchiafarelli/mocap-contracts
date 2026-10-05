import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("harpia_gen", ROOT / "tools/harpia_gen.py")
harpia_gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harpia_gen)

# The worked example of Harpia's USAGE §3 (V4), plus a comment.
EXAMPLE = """
import "file3.harpia";

enum grower { g_a; g_b; g_c = 14; g_d; g_e = 0; }   // one enumerator must be 0

message prince {
    pagination[12] int vari;
    optional int val;
    required map<string,int> b;
    repeteable int scores;
};

stream pull push event message data {
    int i;
    prince val;
    grower car;
    repeteable int tags;
} table_data;

stream pull push event message top_users {
    required string name;
    event message vip_users {
        string family;
    } table_vip_users;
    vip_users myUsers;
    repeteable vip_users members;
} user_table;
"""


def test_parses_the_documented_grammar(tmp_path):
    (tmp_path / "Include").mkdir()
    (tmp_path / "Include" / "x.harpia").write_text(EXAMPLE)
    assert harpia_gen.schema_fields(tmp_path) == {
        "prince": (["vari", "val", "b", "scores"], ["b"]),
        "data": (["i", "val", "car", "tags"], []),
        "top_users": (["name", "myUsers", "members"], ["name"]),
        "vip_users": (["family"], []),
    }
