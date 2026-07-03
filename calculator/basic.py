
"""Basic Mathematical Operations Module
This module provides basic mathematical operations 
such as addition, subtraction, multiplication, and division.
"""

def add(a:int,b:int):
    """Returns the sum of all provided arguments.
     Example: add(a=5, b=3) returns 8."""

    return a + b
def subtract(a:int,b:int):
    """Returns the difference of all provided arguments.
    Example: subtract(a=5, b=3) returns 2."""

    return a - b

def multiply(a:int,b:int):
    """Returns the product of all provided arguments.
    Example: multiply(a=5, b=3) returns 15."""

    return a * b
def divide(a:int,b:int):
    """Returns the quotient of all provided arguments.
    Example: divide(a=6, b=3) returns 2."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a:int,b:int):
    """Returns the modulus of all provided arguments.
    Example: modulus(a=5, b=3) returns 2."""

    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b