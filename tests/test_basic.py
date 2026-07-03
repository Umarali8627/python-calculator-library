import calculator as calc


def test_add():
    assert calc.add(5, 3) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(0, 0) == 0
def test_multiply():
    assert calc.multiply(5, 3) == 15
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 0) == 0

def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, 3) == -2
    try:
        calc.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
def test_modulus():
    assert calc.modulus(5, 3) == 2
    assert calc.modulus(10, 3) == 1
    try:
        calc.modulus(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot perform modulus by zero."
def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
def test_square_root():
    assert calc.square_root(9) == 3
    try:
        calc.square_root(-1)
    except ValueError as e:
        assert str(e) == "Cannot compute square root of negative number."
def test_factorial():
    assert calc.factorial(5) == 120
    assert calc.factorial(0) == 1
    try:
        calc.factorial(-1)
    except ValueError as e:
        assert str(e) == "Cannot compute factorial of negative number."
def test_percentage():
    assert calc.percentage(50, 200) == 25.0
    try:
        calc.percentage(50, 0)
    except ValueError as e:
        assert str(e) == "Total cannot be zero for percentage calculation."

