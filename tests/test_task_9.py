# coding=utf-8
import pytest
from task_9 import Task


def test_raise():
    assert isinstance(Task(), Exception)
    err = Task()
    with pytest.raises(Task) as e:
        raise err
    e.match("whars ma mone dude?")
