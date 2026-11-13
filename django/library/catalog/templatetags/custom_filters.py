from django import template

register = template.Library()


@register.filter
def format_currency(value):
    """
    Форматирует число как цену: 1234 превращает в "1 234 ₽".

    Аргументы:
        value (int | float): сумма, которую нужно показать.

    Возвращает:
        str: цена с пробелами между тысячами и знаком рубля.
    """
    text = f"{value:,.0f}".replace(",", " ")
    return text + " ₽"
