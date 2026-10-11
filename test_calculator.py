"""Тесты для функций калькулятора."""

import unittest

from calculator import add_numbers, divide


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


class TestDivide(unittest.TestCase):
    """Тесты функции divide."""

    def test_divide_numbers(self):
        """Деление двух чисел."""
        self.assertEqual(divide(10, 4), 2.5)

    def test_divide_by_zero_raises_value_error(self):
        """Деление на ноль должно вызывать понятную ошибку."""
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
