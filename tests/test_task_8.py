# coding=utf-8
import pytest
from task_8 import Task


class Class1(Task):
    def name(self):
        return 'Class1'


class Class2(Task):
    def make_noise(self):
        return "noise"


class Class3(Task):
    def make_noise(self): return "noise"

    @property
    def name(self): return 'Class3'


@pytest.mark.parametrize("cls", [Class1, Class2])
def test_raise(cls):
    with pytest.raises(TypeError):
        cls()
    Class3()
