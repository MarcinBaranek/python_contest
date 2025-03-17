# coding=utf-8
import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def fib(n) -> int:
    """returns the n-th element of the Fibonacci sequence.

    >>> fib(0)
    1
    >>> fib(1)
    1
    >>> fib(5) == fib(4) + fib(3)
    True
    """
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
