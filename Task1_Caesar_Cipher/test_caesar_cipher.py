"""Тесты шифра Цезаря."""

import unittest

from caesar_cipher import (
    caesar_decrypt,
    caesar_encrypt,
    detect_alphabet,
    RU_ALPHABET,
)


class TestDetectAlphabet(unittest.TestCase):
    """Тесты автоопределения языка."""

    def test_detects_english(self):
        """Английский текст распознаётся."""
        self.assertEqual(
            detect_alphabet("Hello world"), "abcdefghijklmnopqrstuvwxyz"
        )

    def test_detects_russian(self):
        """Русский текст распознаётся."""
        self.assertEqual(detect_alphabet("Привет мир"), RU_ALPHABET)

    def test_no_letters(self):
        """Текст без букв не относится ни к одному языку."""
        self.assertIsNone(detect_alphabet("123 !?"))


class TestCaesarCipher(unittest.TestCase):
    """Тесты шифрования и расшифровки."""

    def test_encrypt_english(self):
        """Шифрование английского текста с сохранением регистра."""
        self.assertEqual(caesar_encrypt("Abc, xyz!", 3), "Def, abc!")

    def test_encrypt_russian(self):
        """Шифрование русского текста с переходом через конец алфавита."""
        self.assertEqual(caesar_encrypt("Ящик", 1), "Аъйл")

    def test_decrypt_reverts_encrypt(self):
        """Расшифровка возвращает исходный текст на обоих языках."""
        for text in ("Hello, World!", "Привет, мир!"):
            with self.subTest(text=text):
                encrypted = caesar_encrypt(text, 7)
                self.assertEqual(caesar_decrypt(encrypted, 7), text)

    def test_digits_and_spaces_untouched(self):
        """Цифры и пробелы остаются без изменений."""
        self.assertEqual(caesar_encrypt("a 1 b", 1), "b 1 c")

    def test_large_and_negative_shift(self):
        """Сдвиг больше длины алфавита и отрицательный сдвиг работают."""
        self.assertEqual(caesar_encrypt("abc", 29), "def")
        self.assertEqual(caesar_encrypt("abc", -1), "zab")


if __name__ == "__main__":
    unittest.main()
