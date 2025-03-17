# coding=utf-8
import pytest
from task_11 import Task

def test_raise():
    class Base:
        def noise(self): return "how"

    class Child(Base, metaclass=Task):
        pass

    assert not "noise" in dir(Child)
