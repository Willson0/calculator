# calculator

Простой калькулятор на Python с примерами работы с виртуальным окружением, Git и отладкой.

## Установка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Проверка окружения

```bash
python check_env.py
```

## Форматирование и проверка стиля (PEP 8)

```bash
pip install black flake8
black calculator.py test_calculator.py check_env.py
flake8 calculator.py test_calculator.py check_env.py
```

## Тесты

```bash
python -m unittest -v test_calculator
python -m doctest -v calculator.py
```

## Отладка

Ошибка деления на ноль найдена с помощью отладчика pdb:

```bash
python -m pdb -c continue calculator.py
```

Полезные команды pdb: `n` (следующая строка), `s` (войти в функцию), `p a, b` (вывести значения переменных), `c` (продолжить), `q` (выйти).
