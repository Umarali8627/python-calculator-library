# Calculator Library

A simple and lightweight Python calculator library that provides basic and advanced mathematical operations.

## Features

### Basic Operations

* Addition
* Subtraction
* Multiplication
* Division
* Modulus

### Advanced Operations

* Power
* Square Root
* Factorial
* Percentage

---

## Project Structure

```text
Calculator_library/
│
├── calculator/
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
│
├── tests/
│   └── test_basic.py
│
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/calculator-library.git
```

Move into the project directory:

```bash
cd Calculator_library
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install the package in editable mode:

```bash
pip install -e .
```

---

## Usage

```python
import calculator as calc

print(calc.add(10, 20))
print(calc.subtract(20, 5))
print(calc.multiply(5, 4))
print(calc.divide(20, 4))
print(calc.modulus(17, 5))

print(calc.power(2, 8))
print(calc.square_root(81))
print(calc.factorial(5))
print(calc.percentage(45, 60))
```

---

## Running Tests

Install pytest if it is not already installed:

```bash
pip install pytest
```

Run all tests:

```bash
pytest
```

---

## Requirements

* Python 3.10+
* pytest (for testing)

---

## Version

Current Version: **1.0.0**

---

## License

This project is licensed under the MIT License.

---

## Author

**Umar Ali**

Built as a learning project to understand:

* Python package development
* Module organization
* Unit testing with pytest
* Python packaging
* Clean code practices
