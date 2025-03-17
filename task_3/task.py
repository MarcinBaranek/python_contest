# coding=utf-8
from typing import Iterable


def merge_two_collections(
        first_collection: Iterable[int],
        second_collection: Iterable[int]
) -> list[int]:
    """merge two iterable collections and returns sorted result.

    Returns a sorted list which contains all items from both collections.

    Examples:
    >>> merge_two_collections((1, 2, 3), {3, 4, 5})
    [1, 2, 3, 3, 4, 5]
    """
    return sorted(list(first_collection) + list(second_collection))
