import pytest

@pytest.fixture(scope="module")
def none_fixture():
    return None
