# coding=utf-8


def args_adder(argument_name, argument_value):
    """Decorator adding to the decorated function keyword argument.

    Examples:
    >>> @args_adder('start', 13)
    ... def total(items, start): return sum(items) + start
    >>> total([1, 2, 3])
    19
    >>> total([1, 2])
    16
    """
    pass
