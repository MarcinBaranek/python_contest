# coding=utf-8
import pytest
from task_13 import Task


def test_raise():
    obj = Task()
    assert obj() == ([], {})
    assert obj(1, 2) == ([1, 2], {})
    assert obj(1, 3, a=3, b=4) == ([1, 3], {'a': 3, 'b': 4})
