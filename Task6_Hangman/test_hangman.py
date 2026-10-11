"""Тесты игры «Виселица»."""

import unittest

from hangman import HANGMAN_STAGES, is_valid_guess, mask_word


class TestMaskWord(unittest.TestCase):
    """Тесты отображения слова с пропусками."""

    def test_nothing_guessed(self):
        """Без угаданных букв видны только подчёркивания."""
        self.assertEqual(mask_word("кот", set()), "_ _ _")

    def test_some_letters_guessed(self):
        """Угаданные буквы открываются на своих местах."""
        self.assertEqual(mask_word("кот", {"о"}), "_ о _")


class TestIsValidGuess(unittest.TestCase):
    """Тесты проверки ввода игрока."""

    def test_single_russian_letter(self):
        """Одна русская буква — правильный ввод."""
        self.assertTrue(is_valid_guess("а"))

    def test_invalid_inputs(self):
        """Цифры, латиница, пустая строка и несколько букв — неверно."""
        for bad in ("", "ab", "1", "ы2", "a"):
            with self.subTest(value=bad):
                self.assertFalse(is_valid_guess(bad))


class TestStages(unittest.TestCase):
    """Тесты рисунков виселицы."""

    def test_stage_count(self):
        """Рисунков столько, сколько возможных ошибок плюс начальный."""
        self.assertEqual(len(HANGMAN_STAGES), 7)


if __name__ == "__main__":
    unittest.main()
