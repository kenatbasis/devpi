
from devpi_common.validation import *
import pytest

def names(*args):
    return pytest.mark.parametrize("name", args)

class TestValidateMetadata:
    @names("hello", "hello-xyz", "hello1-xyz", "hello_xyz")
    def test_valid_names(self, name):
        validate_metadata(data=dict(name=name, version="1.0"))

    @names("hello_", "hello-", "-hello", "_hello1", "hel%lo",
           "hello#", "hello<",)
    def test_invalid(self, name):
        pytest.raises(ValueError, lambda:
            validate_metadata(data=dict(name=name, version="1.0")))
