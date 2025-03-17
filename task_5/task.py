# coding=utf-8


def sort_by_value(dictionary: dict[str, int]) -> list[str]:
    """Returns list with sorted keys by the value.

    Examples:
    >>> sort_by_value({"one": 1, "two": 2})
    ["one", "two"]
    """
    return [item[0] for item in sorted(dictionary.items(), key=lambda x: x[1])]
