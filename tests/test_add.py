import unittest

from add import add

def add(a, b, operation):
    """Calculate using addition"""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    if operation == "+":
        return a + b
class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(add(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(add(-5, -3, "+"), -8)

    def test_addition_positive_and_negative(self):
        self.assertEqual(add(-5, 3, "+"), -2)

    def test_addition_with_zero(self):
        self.assertEqual(add(5, 0, "+"), 5)

    def test_addition_decimal_numbers(self):
        self.assertAlmostEqual(add(1.5, 2.5, "+"), 4.0)

if __name__ == "__main__":
    unittest.main()