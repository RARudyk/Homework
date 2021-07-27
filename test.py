import pytest
from part_1_doctest import Calc

@pytest.fixture()
def test_sum():
    assert Calc.sum(1, 1) == 2
