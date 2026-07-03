
"""Advanced Mathematical Operations Module
This module provides advanced mathematical operations 
such as power, square root, and factorial and percentage.
"""

def power(a:int,power:int):
    """Returns the result of raising a to the power of power.
    Example: power(a=2, power=3) returns 8."""

    return a ** power
def square_root(a:int):
    """Returns the square root of the provided argument.
    Example: square_root(a=9) returns 3."""

    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return a ** 0.5

def factorial(a:int):
    """Returns the factorial of the provided argument.
    Example: factorial(a=5) returns 120."""

    if a < 0:
        raise ValueError("Cannot compute factorial of negative number.")
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result
def percentage(value:int, total:int):
    """Returns the percentage of value with respect to total.
    Example: percentage(value=50, total=200) returns 25.0."""

    if total == 0:
        raise ValueError("Total cannot be zero for percentage calculation.")
    return (value / total) * 100


