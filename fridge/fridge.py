"""Учёт продуктов в холодильнике: добавление, поиск и проверка сроков годности."""

import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    """Добавляет партию продукта в холодильник.

    Args:
        items (dict): Словарь вида {название: [партии]}, который изменяется на месте.
        title (str): Название продукта.
        amount (int | Decimal): Количество продукта в этой партии.
        expiration_date (str | None): Срок годности в формате 'ГГГГ-ММ-ДД'
            или None, если срок не указан.

    Raises:
        ValueError: Если expiration_date передан, но не соответствует формату 'ГГГГ-ММ-ДД'.
    """
    if title not in items:
        items[title] = []
    if expiration_date is not None:
        expiration_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def _is_date(text):
    """Проверяет, является ли строка датой в формате 'ГГГГ-ММ-ДД'.

    Args:
        text (str): Строка для проверки.

    Returns:
        bool: True, если строка корректно разбирается как дата, иначе False.
    """
    try:
        dt.datetime.strptime(text, DATE_FORMAT)
    except ValueError:
        return False
    return True


def _parse_amount(text):
    """Преобразует строку с количеством в число.

    Целые числа возвращаются как int, остальные (например, '0.5') как Decimal.

    Args:
        text (str): Строка с количеством.

    Returns:
        int | Decimal: Распознанное количество.

    Raises:
        decimal.InvalidOperation: Если строка не является ни целым, ни десятичным числом.
    """
    try:
        return int(text)
    except ValueError:
        return Decimal(text)


def add_by_note(items, note):
    """Добавляет продукты из текстовой заметки, где каждая строка описывает одну партию.

    Формат строки: '<название> <количество> [<срок годности>]', где название может
    содержать пробелы, а срок годности указывается в формате 'ГГГГ-ММ-ДД'.
    Пустые строки пропускаются.

    Args:
        items (dict): Словарь продуктов, который изменяется на месте.
        note (str): Многострочный текст с описанием продуктов.

    Raises:
        ValueError: Если в строке нет названия или количества.
    """
    for line in note.splitlines():
        parts = line.split()
        if not parts:
            continue
        expiration_date = None
        if len(parts) >= 3 and _is_date(parts[-1]):
            expiration_date = parts.pop()
        if len(parts) < 2:
            raise ValueError(f'Некорректная строка: {line!r}')
        amount = _parse_amount(parts.pop())
        title = ' '.join(parts)
        add(items, title, amount, expiration_date)


def find(items, needle):
    """Ищет продукты, в названии которых есть заданное слово.

    Args:
        items (dict): Словарь продуктов.
        needle (str): Искомая подстрока. Регистр не учитывается.

    Returns:
        list[str]: Названия продуктов, подходящих под запрос, в порядке хранения в словаре.
    """
    needle = needle.lower()
    return [title for title in items if needle in title.lower()]


def get_amount(items, needle):
    """Считает суммарное количество всех продуктов, в названии которых есть заданное слово.

    Args:
        items (dict): Словарь продуктов.
        needle (str): Искомая подстрока. Регистр не учитывается.

    Returns:
        Decimal: Общее количество по всем найденным партиям (0, если ничего не найдено).
    """
    product_amount = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            product_amount += part['amount']
    return product_amount


def get_expired(items, in_advance_days=0):
    """Находит продукты, срок годности которых уже истёк или истекает в ближайшие дни.

    Партии без срока годности (None) не учитываются.

    Args:
        items (dict): Словарь продуктов.
        in_advance_days (int): На сколько дней вперёд смотреть. По умолчанию 0,
            то есть проверяются только уже испорченные продукты.

    Returns:
        list[tuple[str, Decimal]]: Пары (название продукта, суммарное количество
            просроченных или скоро просроченных партий). Продукты с нулевым
            количеством не включаются.
    """
    result = []
    today = dt.date.today()
    border = today + dt.timedelta(days=in_advance_days)
    for title, parts in items.items():
        amount = Decimal('0')
        for part in parts:
            expiration_date = part['expiration_date']
            if expiration_date is not None and expiration_date <= border:
                amount += part['amount']
        if amount > 0:
            result.append((title, amount))
    return result
