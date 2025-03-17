# coding=utf-8
import pytest
from task_14 import args_adder


def method(items, start):
    """docstring for method."""
    return sum(items) + start

def test_raise():
    for start in (0, -10, 13, 20):
        m = args_adder("start", 0)(method)
        assert m([1, 2, 3]) == start + 6
    assert m.__doc__ == """docstring for method."""
