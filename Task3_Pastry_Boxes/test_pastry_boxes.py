"""Тесты отчёта о расфасовке пирожных."""

import io
import unittest
from contextlib import redirect_stdout

from pastry_boxes import print_pack_report


def capture_report(count):
    """Возвращает список строк отчёта для count пирожных."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print_pack_report(count)
    return buffer.getvalue().splitlines()


class TestPrintPackReport(unittest.TestCase):
    """Тесты отчёта о расфасовке."""

    def test_report_for_ten(self):
        """Отчёт для 10 пирожных содержит все варианты."""
        self.assertEqual(
            capture_report(10),
            [
                "10 - расфасуем по 5",
                "9 - расфасуем по 3",
                "8 - не заказываем!",
                "7 - не заказываем!",
                "6 - расфасуем по 3",
                "5 - расфасуем по 5",
                "4 - не заказываем!",
                "3 - расфасуем по 3",
                "2 - не заказываем!",
                "1 - не заказываем!",
            ],
        )

    def test_number_divisible_by_both(self):
        """Число, которое делится и на 3, и на 5, — отдельный случай."""
        self.assertIn("15 - расфасуем по 3 или по 5", capture_report(15))

    def test_invalid_input_raises(self):
        """Для чисел меньше двух и для не-целых чисел — ошибка."""
        for bad in (1, 0, -5, 2.5, "10"):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    print_pack_report(bad)


if __name__ == "__main__":
    unittest.main()
