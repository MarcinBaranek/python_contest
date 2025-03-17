# coding=utf-8


class Task:
    """Metaclass ignoring the inheritance

    Examples:
    >>> class Base:
    ...    def noise(self): return "how"
    >>> class Child(Base, metaclass=Task):
    ...     pass
    >>> "noise" in dir(Child)
    Flase
    """
