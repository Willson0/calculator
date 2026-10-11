"""Тесты конвертера римских цифр."""

import unittest

from roman_numerals import int_to_roman, roman_to_int

ROMAN_TESTS = {
    "IV": 4,
    "IX": 9,
    "XLII": 42,
    "XCIX": 99,
    "MMXXIII": 2023,
}


class TestRomanToInt(unittest.TestCase):
    """Тесты перевода римских цифр в обычные."""

    def test_examples(self):
        """Примеры из задания переводятся правильно."""
        for roman, number in ROMAN_TESTS.items():
            with self.subTest(roman=roman):
                self.assertEqual(roman_to_int(roman), number)

    def test_lowercase_is_accepted(self):
        """Строчные буквы тоже принимаются."""
        self.assertEqual(roman_to_int("mcmxc"), 1990)

    def test_invalid_roman_raises(self):
        """Некорректные записи вызывают ошибку."""
        for bad in ("", "IIII", "VX", "ABC", "MMMM"):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    roman_to_int(bad)


class TestIntToRoman(unittest.TestCase):
    """Тесты перевода обычных чисел в римские."""

    def test_examples(self):
        """Обратный перевод для примеров из задания."""
        for roman, number in ROMAN_TESTS.items():
            with self.subTest(number=number):
                self.assertEqual(int_to_roman(number), roman)

    def test_round_trip_all_values(self):
        """Все числа от 1 до 3999 переводятся туда и обратно."""
        for number in range(1, 4000):
            self.assertEqual(roman_to_int(int_to_roman(number)), number)

    def test_out_of_range_raises(self):
        """Числа вне диапазона 1–3999 — ошибка."""
        for bad in (0, -1, 4000):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    int_to_roman(bad)


if __name__ == "__main__":
    unittest.main()
