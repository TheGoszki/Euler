from euler.eluer_01.euler_01 import MultiplesOf3And5 as Multiples
import pytest


def test_multiplies_of_3_and_5():
    assert Multiples().multiples_of_3_and_5(10) == 23
