import pytest
from my_calculadora.modules.basic_math import *


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 6),
        (5, 5, 10),
        (5, -10, -5),
        (5, 15, 20),
        (5, -2, 3)
    ]

)
def test_add(input_num1, input_num2, expected):
    assert suma(input_num1, input_num2) == expected


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 4),
        (5, 5, 0),
        (5, -10, 15),
        (5, 15, -10),
        (5, -2, 7)
    ]

)
def test_resta(input_num1, input_num2, expected):
    assert resta(input_num1, input_num2) == expected
