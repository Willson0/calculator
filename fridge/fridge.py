import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    """Добавляет партию продукта `title` в словарь `items`."""
    if title not in items:
        items[title] = []
    if expiration_date is not None:
        expiration_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def _is_date(text):
    try:
        dt.datetime.strptime(text, DATE_FORMAT)
    except ValueError:
        return False
    return True


def _parse_amount(text):
    try:
        return int(text)
    except ValueError:
        return Decimal(text)


def add_by_note(items, note):
    """Разбирает строки вида «название количество [год-месяц-день]» и добавляет их в `items`."""
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
    """Возвращает названия продуктов, в которых есть подстрока `needle` (без учёта регистра)."""
    needle = needle.lower()
    return [title for title in items if needle in title.lower()]


def get_amount(items, needle):
    """Возвращает суммарное количество продуктов, в названии которых есть `needle`."""
    product_amount = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            product_amount += part['amount']
    return product_amount


def get_expired(items, in_advance_days=0):
    """Возвращает список (название, количество) для партий с истекающим сроком годности."""
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
