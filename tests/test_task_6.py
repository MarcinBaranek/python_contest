# coding=utf-8
import pytest
from task_6 import Task


@pytest.mark.parametrize(
    "dictionary,expected",
    [
        ({"one": 1, "two": 2}, [1, 2]),
        ({"A": 12, "B": 13, "C": -1}, [-1, 12, 13]),
        ({"A": 1, "B": 2, "C": 13}, [1, 2, 3]),
    ]
)
def test_filter_prime_numbers(dictionary, expected):
    assert [e for e in Task(dictionary)] == expected
