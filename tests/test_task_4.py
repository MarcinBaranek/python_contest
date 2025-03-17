# coding=utf-8
import pytest
from task_4 import remove_duplicates


@pytest.mark.parametrize(
    "items,expected",
    [
        (range(5), [0, 1, 2, 3, 4]),
        ((x for x in ((1, 2), (1, 2), 3, 5)), [(1, 2), 3, 5]),
        ({-1: 3, 0: 12, "LAPS": 12}, [-1, 0, "LAPS"]),
    ]
)
def test_filter_prime_numbers(items, expected):
    result = remove_duplicates(items)
    for item in expected:
        assert item in result
