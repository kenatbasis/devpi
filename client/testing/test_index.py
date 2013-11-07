
import pytest
from devpi.index import *

def test_index_show_empty(loghub):
    with pytest.raises(SystemExit):
        index_show(loghub, None)
    loghub._getmatcher().fnmatch_lines("*no index specified*")

def test_parse_keyvalue_spec_index(loghub):
    kvdict = parse_keyvalue_spec_index(loghub, ["bases=x,y"])
    assert kvdict["bases"] == ["x", "y"]
    kvdict = parse_keyvalue_spec_index(loghub, ["bases="])
    assert kvdict["bases"] == []

