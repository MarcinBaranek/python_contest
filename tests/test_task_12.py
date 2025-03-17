# coding=utf-8
import pytest
from task_12 import Task


class TestLogger:
    def log(self, msg): return msg
    def other_method(self, *args, **kwargs): pass

class TestClass:
    logger = Task()


def test_raise():
    obj = TestClass()
    try:
        obj.logger.any_maethod()
        obj.logger.random_meafafaefqwerqwrufsad()
        obj.logger.asfasfqwreooddfv
    except AttributeError as e:
        assert False, "got unexpected exception: {}".format(e)
    obj.logger = TestLogger()
    assert obj.logger.log("msg") == "msg"
    assert obj.logger.other_method("msg") is None
    with pytest.raises(AttributeError):
        obj.logger.random_method()
