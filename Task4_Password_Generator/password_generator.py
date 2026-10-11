"""Генератор сложных паролей с настройками и простым меню в терминале.

Пароль собирается криптографически стойким генератором ``secrets``,
а не ``random``: для паролей это важно.
"""

import secrets
import string
from dataclasses import dataclass

# ANSI-коды цветов для оформления терминала
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

MIN_LENGTH = 4
DEFAULT_LENGTH = 16


@dataclass
class PasswordSettings:
    """Настройки пароля.

    Attributes:
        length (int): Длина пароля.
        use_lower (bool): Использовать строчные буквы.
        use_upper (bool): Использовать заглавные буквы.
        use_digits (bool): Использовать цифры.
        use_special (bool): Использовать спецсимволы.
    """

    length: int = DEFAULT_LENGTH
    use_lower: bool = True
    use_upper: bool = True
    use_digits: bool = True
    use_special: bool = True


def enabled_character_sets(settings):
    """Возвращает наборы символов, которые включены в настройках.

    Args:
        settings (PasswordSettings): Настройки пароля.

    Returns:
        list[str]: Строки с допустимыми символами для каждого включённого
        набора.
    """
    sets = []
    if settings.use_lower:
        sets.append(string.ascii_lowercase)
    if settings.use_upper:
        sets.append(string.ascii_uppercase)
    if settings.use_digits:
        sets.append(string.digits)
    if settings.use_special:
        sets.append(string.punctuation)
    return sets


def generate_password(settings):
    """Генерирует пароль по настройкам.

    Из каждого включённого набора символов в пароль попадает минимум
    один символ, остальные выбираются случайно из всех наборов.

    Args:
        settings (PasswordSettings): Настройки пароля.

    Returns:
        str: Сгенерированный пароль.

    Raises:
        ValueError: Если не выбран ни один набор символов, длина меньше
            минимальной или меньше количества выбранных наборов.

    Example:
        >>> len(generate_password(PasswordSettings(length=12)))
        12
    """
    sets = enabled_character_sets(settings)
    if not sets:
        raise ValueError("Выберите хотя бы один тип символов")
    if settings.length < max(MIN_LENGTH, len(sets)):
        raise ValueError(
            f"Длина должна быть не меньше {max(MIN_LENGTH, len(sets))}"
        )

    # Один обязательный символ из каждого набора
    password_chars = [secrets.choice(chars) for chars in sets]

    # Остальные символы — из объединения всех наборов
    all_chars = "".join(sets)
    while len(password_chars) < settings.length:
        password_chars.append(secrets.choice(all_chars))

    # Перемешиваем, чтобы обязательные символы не стояли в начале
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def show_menu(settings):
    """Печатает главное меню с текущими настройками."""
    print(f"\n{BOLD}{CYAN}=== Генератор паролей ==={RESET}")
    print(f"  Длина:            {settings.length}")
    print(f"  Строчные буквы:   {_flag(settings.use_lower)}")
    print(f"  Заглавные буквы:  {_flag(settings.use_upper)}")
    print(f"  Цифры:            {_flag(settings.use_digits)}")
    print(f"  Спецсимволы:      {_flag(settings.use_special)}")
    print()
    print("  1 — сгенерировать пароль")
    print("  2 — изменить длину")
    print("  3 — переключить строчные буквы")
    print("  4 — переключить заглавные буквы")
    print("  5 — переключить цифры")
    print("  6 — переключить спецсимволы")
    print("  0 — выход")


def _flag(value):
    """Возвращает цветную отметку вкл/выкл для меню."""
    return f"{GREEN}вкл{RESET}" if value else f"{RED}выкл{RESET}"


def main():
    """Главный цикл программы: меню, выбор пункта и вывод результата."""
    settings = PasswordSettings()

    while True:
        show_menu(settings)
        choice = input(f"{YELLOW}Выберите пункт: {RESET}").strip()

        if choice == "0":
            print("До встречи!")
            break
        if choice == "1":
            try:
                password = generate_password(settings)
            except ValueError as error:
                print(f"{RED}Ошибка: {error}{RESET}")
                continue
            print(f"\n{BOLD}Ваш пароль:{RESET} {GREEN}{password}{RESET}")
        elif choice == "2":
            _change_length(settings)
        elif choice in ("3", "4", "5", "6"):
            _toggle(settings, choice)
        else:
            print(f"{RED}Такого пункта нет{RESET}")


def _change_length(settings):
    """Спрашивает новую длину пароля и сохраняет её в настройках."""
    raw = input("Новая длина пароля: ").strip()
    if not raw.isdigit() or int(raw) < MIN_LENGTH:
        print(f"{RED}Введите целое число не меньше {MIN_LENGTH}{RESET}")
        return
    settings.length = int(raw)


def _toggle(settings, choice):
    """Переключает один из наборов символов по номеру пункта меню."""
    field = {
        "3": "use_lower",
        "4": "use_upper",
        "5": "use_digits",
        "6": "use_special",
    }[choice]
    setattr(settings, field, not getattr(settings, field))


if __name__ == "__main__":
    main()
