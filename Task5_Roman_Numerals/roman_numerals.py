"""Конвертер обычных и римских цифр.

Римские цифры поддерживаются в диапазоне от I (1) до MMMCMXCIX (3999).
"""

import re

# Пары (значение, римская запись), от большего к меньшему.
# Вычитательные пары вроде IV и CM — тоже в таблице.
ROMAN_VALUES = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

# Строгий шаблон корректной римской записи до 3999
ROMAN_PATTERN = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)


def int_to_roman(number):
    """Переводит обычное число в римскую запись.

    Args:
        number (int): Число от 1 до 3999.

    Returns:
        str: Римская запись числа.

    Raises:
        ValueError: Если число вне диапазона от 1 до 3999.

    Example:
        >>> int_to_roman(2023)
        'MMXXIII'
    """
    if not isinstance(number, int) or not 1 <= number <= 3999:
        raise ValueError("Число должно быть целым от 1 до 3999")

    result = []
    # Жадно берём самые большие пары, пока число не станет нулём
    for value, symbol in ROMAN_VALUES:
        count, number = divmod(number, value)
        result.append(symbol * count)
    return "".join(result)


def roman_to_int(roman):
    """Переводит римскую запись в обычное число.

    Args:
        roman (str): Римская запись, например "XLII".

    Returns:
        int: Значение числа.

    Raises:
        ValueError: Если строка не является корректной римской записью.

    Example:
        >>> roman_to_int("XLII")
        42
    """
    text = roman.upper()
    if not text or not ROMAN_PATTERN.match(text):
        raise ValueError(f"Некорректная римская запись: {roman!r}")

    symbol_values = {symbol: value for value, symbol in ROMAN_VALUES}
    total = 0
    # Если текущая цифра меньше следующей, это вычитание (IV = 4, XL = 40)
    for index, symbol in enumerate(text):
        value = symbol_values[symbol]
        next_value = (
            symbol_values[text[index + 1]] if index + 1 < len(text) else 0
        )
        total += -value if value < next_value else value
    return total


if __name__ == "__main__":
    roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
    for roman in roman_tests:
        print(f"{roman} -> {roman_to_int(roman)}")

    number = int(input("Введите число от 1 до 3999: "))
    print(f"{number} -> {int_to_roman(number)}")
