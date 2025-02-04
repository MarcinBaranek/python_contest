# coding=utf-8
import pytest
from task_2 import filter_prime_numbers


@pytest.mark.parametrize(
    "numbers,expected",
    [
        (range(10), [0, 1, 4, 6, 8, 9]),
        ((3, 5, 7, 13, 11), [])
    ]
)
def test_filter_prime_numbers(numbers, expected):
    assert filter_prime_numbers(numbers) == expected
