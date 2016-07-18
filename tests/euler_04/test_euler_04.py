from euler.euler_04.euler_04 import *
import pytest


@pytest.mark.parametrize(
    ['param_value', 'param_result'],
    [
        (6535353, False),
        (123454321, True),
        (2002, True)
    ]
)
def test_is_palindrome(param_value, param_result):
    assert is_palindromic(param_value) == param_result
