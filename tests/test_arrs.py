from utils import arrs
import pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([1, 2, 3, 4, 5], 6, "test") == 5

@pytest.fixture
def bez_raznici():
    return [1, 2, 3, 4]

@pytest.fixture
def be_raznici_two():
    return [1, 2, 3]
def test_slice(bez_raznici, be_raznici_two):
    assert arrs.my_slice(bez_raznici, 1, 3) == [2, 3]
    assert arrs.my_slice(be_raznici_two, 1) == [2, 3]
    assert arrs.my_slice(bez_raznici, -1) == [4]
    assert arrs.my_slice([], 5, 1) == []
    assert arrs.my_slice(bez_raznici, -5) == [1, 2, 3, 4]
