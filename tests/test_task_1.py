# coding=utf-8
from task_1 import say_my_name


def test_say_my_name():
    result = say_my_name()
    expected = "Heisenberg"
    assert result == expected
