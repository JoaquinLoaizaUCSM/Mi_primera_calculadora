import pytest
from modules.math_basic.operations_basic import *


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 6),
        (5, 5, 10),
        (5, -10, -5),
        (5.0, 15.3, 20.3),
        (5.3, -2.0, 3.3)
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


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 5),
        (5, -5, -25),
        (5, -10, -50),
        (10, 0.5, 5),
        (0.4, -0.2, -0.08)
    ]
)
def test_multiplicacion(input_num1, input_num2, expected):
    assert mutiplicacion(input_num1, input_num2) == expected


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (10, 5, 2),
        (5, -5, -1.0),
        (100, 10, 10),
        (-10, 2, -5),
        (0.4, -0.2, -2.0)
    ]
)
def test_dividir(input_num1, input_num2, expected):
    assert dividir(input_num1, input_num2) == expected


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (10, 5, 0),
        (20, 10, 0),
        (15, 4, 3),
        (20, 6, 2),
        (0.4, -0.2, 0)
    ]
)
def test_dividir_resto(input_num1, input_num2, expected):
    assert dividir_resto(input_num1, input_num2) == expected
