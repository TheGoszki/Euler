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


@pytest.mark.parametrize(
    ['param_number', 'param_result'],
    [
        (3, True),
        (4, False),
        (6, True),
        (10, False)
    ]
)
def test_is_multiple_of_3(param_number, param_result):
    assert Multiples().is_multiple_of_3(param_number) == param_result


@pytest.mark.parametrize(
    ['param_number', 'param_result'],
    [
        (5, True),
        (1, False),
        (10, True),
        (13, False)
    ]
)
def test_is_multiple_of_5(param_number, param_result):
    assert Multiples().is_multiple_of_5(param_number) == param_result
