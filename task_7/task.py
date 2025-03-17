# coding=utf-8


def interpret_math_text(text: str) -> float:
    """Interpret text to make a calculations.

    Examples:
    >>> interpret_math_text("2+2")
    4
    >>> interpret_math_text("3/4")
    0.75
    >>> interpret_math_text("3*1.1")
    3.3
    >>> interpret_math_text("2-2")
    0
    >>> interpret_math_text("2**2")
    4
    """
    return eval(text)
