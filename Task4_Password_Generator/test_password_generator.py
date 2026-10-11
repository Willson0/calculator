"""Тесты генератора паролей."""

import string
import unittest

from password_generator import (
    PasswordSettings,
    enabled_character_sets,
    generate_password,
)


class TestGeneratePassword(unittest.TestCase):
    """Тесты генерации пароля."""

    def test_length_matches_settings(self):
        """Длина пароля совпадает с настройкой."""
        for length in (4, 12, 40):
            with self.subTest(length=length):
                password = generate_password(PasswordSettings(length=length))
                self.assertEqual(len(password), length)

    def test_contains_every_enabled_set(self):
        """Каждый включённый набор символов есть в пароле."""
        settings = PasswordSettings(length=20)
        for _ in range(50):
            password = generate_password(settings)
            self.assertTrue(any(c in string.ascii_lowercase for c in password))
            self.assertTrue(any(c in string.ascii_uppercase for c in password))
            self.assertTrue(any(c in string.digits for c in password))
            self.assertTrue(any(c in string.punctuation for c in password))

    def test_disabled_sets_are_not_used(self):
        """Выключенные наборы в пароле не появляются."""
        settings = PasswordSettings(
            length=30, use_upper=False, use_special=False
        )
        for _ in range(50):
            password = generate_password(settings)
            self.assertFalse(
                any(c in string.ascii_uppercase for c in password)
            )
            self.assertFalse(any(c in string.punctuation for c in password))

    def test_no_sets_raises(self):
        """Если все наборы выключены, генерация невозможна."""
        settings = PasswordSettings(
            use_lower=False,
            use_upper=False,
            use_digits=False,
            use_special=False,
        )
        with self.assertRaises(ValueError):
            generate_password(settings)

    def test_too_short_length_raises(self):
        """Слишком короткий пароль — ошибка."""
        with self.assertRaises(ValueError):
            generate_password(PasswordSettings(length=2))


class TestEnabledSets(unittest.TestCase):
    """Тесты выбора наборов символов."""

    def test_default_has_four_sets(self):
        """По умолчанию включены все четыре набора."""
        self.assertEqual(len(enabled_character_sets(PasswordSettings())), 4)


if __name__ == "__main__":
    unittest.main()
