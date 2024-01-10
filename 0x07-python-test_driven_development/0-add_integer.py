#!/usr/bin/python3
# 0-add_integer.py
"""Defines addition of integers."""

def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a ((int, (float)): first arg to add to sum.
        b ((int, (float)): second arg to add to sum. Defaults to 98.

    Returns: sum of both values.

    """
    if not isinstance(a, (int, float)):
         a = int(a)
    elif type(a) is not int:
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        b = int(b)
    elif type(b) is not int
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
