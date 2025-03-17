# coding=utf-8


class Task(type):
    """Metaclass ignoring the inheritance

    Examples:
    >>> class Base:
    ...    def noise(self): return "how"
    >>> class Child(Base, metaclass=Task):
    ...     pass
    >>> "noise" in dir(Child)
    Flase
    """
    def __new__(cls, clsname, bases, attrs):
        return type.__new__(cls, clsname, (), attrs)
