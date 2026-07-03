"""
calculator Library
This library provides basic arithmetic operations such as addition, subtraction, multiplication, and division.
It also includes advanced mathematical operations such as power, square root, factorial, and percentage calculations.
"""

from .basic import (
    add,
    subtract,
    multiply,
    divide,
    modulus
)

from .advanced import (
    power,
    square_root,
    factorial,
    percentage
)


__version__ = "1.0.0"