from euler.euler_03.euler_03 import *
import pytest


@pytest.mark.parametrize(
    ['param_value', 'param_result'],
    [
        (29, True),
        (30, False)
    ]
)
def test_is_prime(param_value, param_result):
    assert is_prime(param_value) == param_result


# def test_largest_prime_factor():
#     assert largest_prime_factor(58) == 29
