from euler.eluer_01.euler_01 import MultiplesOf3And5 as Multiples
import pytest


@pytest.mark.parametrize(
    ['param_number', 'param_result'],
    [
        (5, [1, 2, 3, 4, 5]),
    ]
)
def test_get_n_numbers(param_number, param_result):
    assert Multiples().get_n_numbers(param_number) == param_result
