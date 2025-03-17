# coding=utf-8
from typing import Iterable, Hashable


def remove_duplicates(items: Iterable[Hashable]) -> list[Hashable]:
    """Remove duplicated items and returns list with left items.

    Examples:
    >>> remove_duplicates([1, 1, 2, 1, 2])
    [1, 2]
    """
    return list(set(items))
