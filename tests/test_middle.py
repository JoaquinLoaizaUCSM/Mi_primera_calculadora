import pytest
from modules.math_middle import mcd, mcm, factorial, comparaciones


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 5),
        (5, 5, 5),
        (5, -10, 10)
        # (5.0, 15.3, 20.3),
        # (5.3, -2.0, 3.3)
    ]
)
def test_mcm(input_num1, input_num2, expected):
    assert mcm.mcm(input_num1, input_num2) == expected


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 1),
        (5, 5, 5),
        (5, -10, -5)
        # (5.0, 15.3, 76.5),
        # (5.3, -2.0, 3.3)
    ]
)
def test_mcd(input_num1, input_num2, expected):
    assert mcd.mcd(input_num1, input_num2) == expected


@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, 3628800),
        (5, 120),
        (0, 1),
        (-10, 0),
        (1, 1),
        (2, 2)
    ]
)
def test_factorial(input_num, expected):
    assert factorial.factorial(input_num) == expected


@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (5, 1, 5),
        (5, 5, (5, 5)),
        (5, -10, 5),
        (5.0, 15.3, 15.3),
        (5.3, -2.0, 5.3)
    ]
)
def test_comparacion(input_num1, input_num2, expected):
    assert comparaciones.mayor_menor_igual(input_num1, input_num2) == expected






