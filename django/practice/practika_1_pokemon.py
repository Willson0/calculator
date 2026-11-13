"""
Практика #1. Работа с API (PokeAPI).

Программа показывает первых 20 покемонов, затем спрашивает имя
покемона и выводит его тип, вес, рост и способности.
"""

import json
import urllib.request


def get_data(url):
    """
    Отправляет GET-запрос по адресу и возвращает ответ как словарь.

    Аргументы:
        url (str): адрес, по которому нужно получить данные.

    Возвращает:
        dict: данные из ответа сервера, разобранные из JSON.
    """
    request = urllib.request.Request(url, headers={"User-Agent": "student"})
    response = urllib.request.urlopen(request)
    return json.loads(response.read())


def show_first_20():
    """
    Печатает имена первых 20 покемонов, каждое с новой строки.

    Аргументы:
        Нет.

    Возвращает:
        None: ничего не возвращает, только печатает на экран.
    """
    data = get_data("https://pokeapi.co/api/v2/pokemon?limit=20")
    for pokemon in data["results"]:
        print(pokemon["name"])


def show_pokemon(name):
    """
    Печатает имя, тип, вес, рост и способности покемона.

    Аргументы:
        name (str): имя покемона на английском, например "clefairy".

    Возвращает:
        None: ничего не возвращает, только печатает на экран.
    """
    data = get_data("https://pokeapi.co/api/v2/pokemon/" + name)
    print("Имя:", data["name"])
    types = [t["type"]["name"] for t in data["types"]]
    print("Тип:", ", ".join(types))
    print("Вес:", data["weight"] / 10, "кг")
    print("Рост:", data["height"] / 10, "м")
    abilities = [a["ability"]["name"] for a in data["abilities"]]
    print("Способности:", ", ".join(abilities))


show_first_20()
name = input("Имя покемона: ")
show_pokemon(name)
