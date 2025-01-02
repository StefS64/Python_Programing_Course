import pytest
from unittest.mock import mock_open, patch
from Fraction import Fraction

@pytest.fixture
def fractions():
    return Fraction(1, 2), Fraction(3, 4), Fraction(-1, 2)

@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 2), Fraction(1, 1)),
    (Fraction(1, 2), Fraction(1, 3), Fraction(5, 6)),
    (Fraction(1, 2), Fraction(-1, 2), Fraction(0, 1)),
])
def test_add(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 2), Fraction(0, 1)),
    (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
    (Fraction(1, 2), Fraction(-1, 2), Fraction(1, 1)),
])
def test_sub(a, b, expected):
    assert a - b == expected

@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 2), Fraction(1, 4)),
    (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
    (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 4)),
])
def test_mul(a, b, expected):
    assert a * b == expected

@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 2), Fraction(1, 1)),
    (Fraction(1, 2), Fraction(1, 3), Fraction(3, 2)),
    (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 1)),
])
def test_truediv(a, b, expected):
    assert a / b == expected

@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 2), True),
    (Fraction(1, 2), Fraction(1, 3), False),
    (Fraction(1, 2), Fraction(-1, 2), False),
])
def test_eq(a, b, expected):
    assert (a == b) == expected

def test_save_load_fraction():
    fraction = Fraction(1, 2)
    mock = mock_open()

    with patch("builtins.open", mock):
        fraction.fractionSaveFile("test.txt")
        mock.assert_called_once_with("test.txt", "w")
        mock().write.assert_called_once_with("1/2")

    with patch("builtins.open", mock):
        mock.return_value.read.return_value = "1/2"
        loaded_fraction = fraction.fractionFromFile("test.txt")
        assert loaded_fraction == fraction