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

## Задачи из лекции

Каждая задача лежит в своей папке и запускается отдельно. Тесты — стандартным `unittest`.

| Папка | Задача | Запуск |
|---|---|---|
| [Task1_Caesar_Cipher](Task1_Caesar_Cipher) | Шифр Цезаря (русский и английский, автоопределение языка) | `python caesar_cipher.py` |
| [Task2_Olympiad_Winners](Task2_Olympiad_Winners) | Тройка победителей олимпиады (`check_winners`) | `python olympiad_winners.py` |
| [Task3_Pastry_Boxes](Task3_Pastry_Boxes) | Расфасовка пирожных по коробкам на 3 и 5 | `python pastry_boxes.py` |
| [Task4_Password_Generator](Task4_Password_Generator) | Генератор паролей с настройками и меню | `python password_generator.py` |
| [Task5_Roman_Numerals](Task5_Roman_Numerals) | Конвертер римских и обычных цифр | `python roman_numerals.py` |
| [Task6_Hangman](Task6_Hangman) | Игра «Виселица» | `python hangman.py` |

Запуск тестов в папке задачи:

```bash
python -m unittest -v
```
