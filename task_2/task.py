# coding=utf-8
from typing import Iterable
import math

def filter_prime_numbers(numbers: Iterable[int]) -> list[int]:
    """Filter prime numbers from a given iterable collections.

    Returns list of numbers which are not a prime numbers.

    Examples:
    >>> filter_prime_numbers(range(10))
    [0, 1, 4, 6, 8, 9]
    """
    result: list[int] = []
    for number in numbers:
        if number < 2:
            result.append(number)
            continue
        need_to_add = False
        for divisor in range(2, int(math.sqrt(number) + 1)):
            if number % divisor == 0:
                need_to_add = True
                break
        if need_to_add:
            result.append(number)
    return result
