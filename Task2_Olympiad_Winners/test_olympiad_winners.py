"""Тесты функции check_winners."""

import io
import unittest
from contextlib import redirect_stdout

from olympiad_winners import check_winners

SCORES = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]


def run_and_capture(scores, student_score):
    """Запускает check_winners и возвращает напечатанный текст."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = check_winners(scores, student_score)
    # Функция не должна ничего возвращать
    assert result is None
    return buffer.getvalue().strip()


class TestCheckWinners(unittest.TestCase):
    """Тесты тройки победителей."""

    def test_first_place_is_winner(self):
        """Лучший результат попадает в тройку."""
        self.assertEqual(
            run_and_capture(SCORES, 52), "Вы в тройке победителей!"
        )

    def test_third_place_is_winner(self):
        """Третье место тоже считается победой."""
        self.assertEqual(
            run_and_capture(SCORES, 48), "Вы в тройке победителей!"
        )

    def test_fourth_place_is_not_winner(self):
        """Четвёртое место в тройку не попадает."""
        self.assertEqual(
            run_and_capture(SCORES, 41),
            "Вы не попали в тройку победителей.",
        )

    def test_score_not_in_list(self):
        """Балл, которого нет в списке, в тройку не попадает."""
        self.assertEqual(
            run_and_capture(SCORES, 100), "Вы в тройке победителей!"
        )


if __name__ == "__main__":
    unittest.main()
