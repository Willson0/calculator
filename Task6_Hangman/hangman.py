"""Игра «Виселица» на русском языке.

Игрок угадывает буквы загаданного слова. Каждая ошибка добавляет
часть виселицы. Если виселица собрана целиком — игра проиграна.
"""

import random

WORDS = [
    "программа",
    "переменная",
    "функция",
    "питон",
    "компьютер",
    "клавиатура",
    "алгоритм",
    "библиотека",
]

# Рисунки виселицы: индекс — количество ошибок
HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

MAX_MISTAKES = len(HANGMAN_STAGES) - 1


def mask_word(word, guessed_letters):
    """Возвращает слово, где неугаданные буквы заменены на «_».

    Args:
        word (str): Загаданное слово.
        guessed_letters (set[str]): Уже названные игроком буквы.

    Returns:
        str: Например, «п _ о г _ а м м а».

    Example:
        >>> mask_word("кот", {"о"})
        '_ о _'
    """
    return " ".join(ch if ch in guessed_letters else "_" for ch in word)


def is_valid_guess(text):
    """Проверяет, что введена ровно одна русская буква.

    Args:
        text (str): Ввод игрока.

    Returns:
        bool: True, если введена одна буква русского алфавита.
    """
    return (
        len(text) == 1 and text.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    )


def play_game(word):
    """Играет одну партию в виселицу.

    Args:
        word (str): Слово, которое нужно угадать.

    Returns:
        bool: True, если игрок победил.
    """
    guessed = set()
    mistakes = 0

    while True:
        print(HANGMAN_STAGES[mistakes])
        print("Слово:", mask_word(word, guessed))
        print("Ошибок:", mistakes, "из", MAX_MISTAKES)

        if all(ch in guessed for ch in word):
            print("Поздравляем, вы победили!")
            return True
        if mistakes == MAX_MISTAKES:
            print(f"Вы проиграли. Загаданное слово: {word}")
            return False

        letter = input("Введите букву: ").strip().lower()
        if not is_valid_guess(letter):
            print("Нужно ввести одну букву русского алфавита.")
            continue
        if letter in guessed:
            print("Эта буква уже была.")
            continue

        guessed.add(letter)
        if letter not in word:
            mistakes += 1


def main():
    """Запускает игру со случайным словом из списка."""
    play_game(random.choice(WORDS))


if __name__ == "__main__":
    main()
