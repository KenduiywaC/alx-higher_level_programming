#!/usr/bin/python3
# 0-add_integer.py
"""Defines addition of integers."""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
