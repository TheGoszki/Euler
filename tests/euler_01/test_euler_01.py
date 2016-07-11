from euler.eluer_01.euler_01 import MultiplesOf3And5 as Multiples
import pytest


@pytest.mark.parametrize(
    ['param_number', 'param_result'],
    [
        (5, [1, 2, 3, 4]),
    ]
)
def test_get_n_numbers(param_number, param_result):
    assert Multiples().get_n_numbers(param_number) == param_result


def test_list_multiplies_of_3_and_5():
    boundary = 10
    multiplies_of_3_and_5 = [3, 5, 6, 9]
    assert Multiples().list_multiplies_of_3_and_5(boundary) == multiplies_of_3_and_5    # noqa


def test_sum_array_of_numbers():
    numbers = [3, 5, 6, 9]
    numbers_sum = 23
    assert Multiples.sum_array_of_numbers(numbers) == numbers_sum
