# coding=utf-8
import pytest
from task_3 import merge_two_collections


@pytest.mark.parametrize(
    "col_1,col_2,expected",
    [
        (range(5), {-1, 0}, [-1, 0, 0, 1, 2, 3, 4]),
        ((x for x in (11, -1, 3, 7, 4)), [], [-1, 3, 4, 7, 11]),
        ({-1: 3, 0: 12}, [0], [-1, 0, 0])
    ]
)
def test_filter_prime_numbers(col_1, col_2, expected):
    assert merge_two_collections(col_1, col_2) == expected
