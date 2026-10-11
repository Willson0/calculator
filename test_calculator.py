"""Тесты для функций калькулятора."""

import unittest

from calculator import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Тесты функции add_numbers."""

    def test_add_positive_numbers(self):
        """Сложение двух положительных чисел."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        """Сложение двух отрицательных чисел."""
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_float_numbers(self):
        """Сложение дробных чисел."""
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()
