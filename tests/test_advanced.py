import pytest
from modules.math_advanced.fibonacci import *


@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, [1, 1, 2, 3, 5, 8]),
        (5, [1, 1, 2, 3]),
        (0, 0),
        (-10, 0),
        (1, 0),
        (2, [1, 1])
    ]
)
def test_fibonacci(input_num, expected):
    assert fibonacci(input_num) == expected
