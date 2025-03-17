# coding=utf-8


class Task:
    """On call retunrs positional and keyword arguments.

    Objects of this class on call return positional arguments as a list and
    keyword arguments. The entire result is in form `tuple[list, dict]`

    The arguments don't play any role.

    Examples:
    >>> obj = Task()
    >>> obj()
    ([], {})
    >>> obj(1, 2)
    ([1, 2], {})
    >>> obj(1, 3, a=3, b=4)
    ([1, 3], {'a': 3, 'b': 4})
    """
    def __call__(self, *args, **kwargs):
        return list(args), kwargs
