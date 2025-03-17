# coding=utf-8
import pytest
from task_7 import interpret_math_text


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2+2", 4),
        ("2-2", 0),
        ("3/3", 1),
        ("2**2", 4),
        ("2+2*2", 6),
    ]
)
def test_filter_prime_numbers(text, expected):
    assert interpret_math_text(text) == expected


@pytest.mark.parametrize("text", ["2/0",])
def test_filter_prime_numbers(text):
    with pytest.raises(Exception):
        interpret_math_text(text)
