# coding=utf-8
import pytest
from task_5 import sort_by_value


@pytest.mark.parametrize(
    "dictionary,expected",
    [
        ({"one": 1, "two": 2}, ["one", "two"]),
        ({"A": 12, "B": 13, "C": -1}, ["C", "A", "B"]),
        ({"A": 1, "B": 2, "C": 13}, ["A", "B", "C"]),
    ]
)
def test_filter_prime_numbers(dictionary, expected):
    assert sort_by_value(dictionary) == expected
