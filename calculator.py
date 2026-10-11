"""Простой калькулятор: сложение, вычитание, умножение и деление."""


def add_numbers(a: float, b: float) -> float:
    """Складывает два числа.

    Args:
        a (float): Первое слагаемое.
        b (float): Второе слагаемое.

    Returns:
        float: Сумма чисел a и b.

    Example:
        >>> add_numbers(2, 3)
        5
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Вычитает второе число из первого.

    Args:
        a (float): Уменьшаемое.
        b (float): Вычитаемое.

    Returns:
        float: Разность a - b.

    Example:
        >>> subtract_numbers(5, 3)
        2
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Перемножает два числа.

    Args:
        a (float): Первый множитель.
        b (float): Второй множитель.

    Returns:
        float: Произведение a * b.

    Example:
        >>> multiply_numbers(4, 2.5)
        10.0
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Делит первое число на второе.

    Args:
        a (float): Делимое.
        b (float): Делитель.

    Returns:
        float: Частное a / b.

    Raises:
        ValueError: Если делитель равен нулю.

    Example:
        >>> divide(10, 4)
        2.5
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
