# coding=utf-8


class Task(dict):
    """Dictionary extension iterating over sorted values instead of keys.

    The default behavior of dict is iterating over keys.
    The class change the behavior.

    Examples:
    >>> d = dict(a=1, b=2)
    >>> [e for e in d]
    ["a", "b"]
    >>> task = Task(a=1, b=2)
    >>> [e for e in task]
    [1, 2]
    """
    def __iter__(self):
        return iter(sorted(self.values()))
