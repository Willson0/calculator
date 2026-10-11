"""Шифр Цезаря с поддержкой русского и английского языков.

Язык текста определяется автоматически: считаем буквы каждого алфавита
и выбираем тот, которых больше.
"""

RU_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
EN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def detect_alphabet(text):
    """Определяет, на каком языке написан текст.

    Args:
        text (str): Текст для анализа.

    Returns:
        str | None: Алфавит (RU_ALPHABET или EN_ALPHABET) или None,
        если в тексте нет букв из поддерживаемых алфавитов.
    """
    lower_text = text.lower()
    ru_count = sum(ch in RU_ALPHABET for ch in lower_text)
    en_count = sum(ch in EN_ALPHABET for ch in lower_text)
    if ru_count == 0 and en_count == 0:
        return None
    return RU_ALPHABET if ru_count >= en_count else EN_ALPHABET


def shift_text(text, shift, alphabet):
    """Сдвигает буквы текста внутри заданного алфавита.

    Символы, которых нет в алфавите (цифры, пробелы, знаки), не меняются.
    Регистр букв сохраняется.

    Args:
        text (str): Исходный текст.
        shift (int): Сдвиг. Может быть отрицательным.
        alphabet (str): Алфавит в нижнем регистре.

    Returns:
        str: Текст после сдвига.
    """
    size = len(alphabet)
    result = []
    for ch in text:
        index = alphabet.find(ch.lower())
        if index == -1:
            # Не буква алфавита: оставляем как есть
            result.append(ch)
            continue
        new_ch = alphabet[(index + shift) % size]
        result.append(new_ch.upper() if ch.isupper() else new_ch)
    return "".join(result)


def caesar_encrypt(text, shift):
    """Шифрует текст шифром Цезаря.

    Args:
        text (str): Открытый текст на русском или английском.
        shift (int): Сдвиг вперёд по алфавиту.

    Returns:
        str: Зашифрованный текст.

    Example:
        >>> caesar_encrypt("abc", 3)
        'def'
    """
    alphabet = detect_alphabet(text)
    if alphabet is None:
        return text
    return shift_text(text, shift, alphabet)


def caesar_decrypt(text, shift):
    """Расшифровывает текст шифром Цезаря.

    Расшифровка — это шифрование с обратным сдвигом.

    Args:
        text (str): Зашифрованный текст.
        shift (int): Тот же сдвиг, что использовался при шифровании.

    Returns:
        str: Исходный текст.

    Example:
        >>> caesar_decrypt("def", 3)
        'abc'
    """
    return caesar_encrypt(text, -shift)


def main():
    """Интерактивный режим: выбор действия, текста и сдвига."""
    print("Шифр Цезаря: 1 — шифровать, 2 — расшифровать")
    choice = input("Выберите действие: ").strip()
    if choice not in ("1", "2"):
        print("Нужно ввести 1 или 2.")
        return

    text = input("Введите текст: ")
    try:
        shift = int(input("Введите сдвиг (целое число): "))
    except ValueError:
        print("Сдвиг должен быть целым числом.")
        return

    if choice == "1":
        print("Результат:", caesar_encrypt(text, shift))
    else:
        print("Результат:", caesar_decrypt(text, shift))


if __name__ == "__main__":
    main()
