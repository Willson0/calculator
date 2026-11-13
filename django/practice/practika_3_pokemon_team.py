import json
import urllib.request

team = []


def get_data(name):
    """
    Берёт данные покемона по имени из PokeAPI.

    Аргументы:
        name (str): имя покемона на английском, например "pikachu".

    Возвращает:
        dict: данные покемона, разобранные из JSON.
    """
    url = "https://pokeapi.co/api/v2/pokemon/" + name
    request = urllib.request.Request(url, headers={"User-Agent": "student"})
    response = urllib.request.urlopen(request)
    return json.loads(response.read())


def show_pokemon(name):
    """
    Печатает имя, тип, вес, рост и способности покемона.

    Аргументы:
        name (str): имя покемона на английском.

    Возвращает:
        None: ничего не возвращает, только печатает на экран.
    """
    data = get_data(name)
    print("Имя:", data["name"])
    types = [t["type"]["name"] for t in data["types"]]
    print("Тип:", ", ".join(types))
    print("Вес:", data["weight"] / 10, "кг")
    print("Рост:", data["height"] / 10, "м")
    abilities = [a["ability"]["name"] for a in data["abilities"]]
    print("Способности:", ", ".join(abilities))
    print()


def add_pokemon():
    """
    Спрашивает имя покемона и добавляет его в команду, если его там ещё нет.

    Аргументы:
        Нет. Имя вводится с клавиатуры через input().

    Возвращает:
        None: ничего не возвращает, меняет список team.
    """
    name = input("Имя покемона: ").lower()
    if name not in team:
        team.append(name)
    print(name, "добавлен")


def remove_pokemon():
    """
    Спрашивает имя покемона и удаляет его из команды.

    Аргументы:
        Нет. Имя вводится с клавиатуры через input().

    Возвращает:
        None: ничего не возвращает, меняет список team.
    """
    name = input("Имя покемона: ").lower()
    team.remove(name)
    print(name, "удалён")


def show_team():
    """
    Печатает подробную информацию о всех покемонах команды.

    Аргументы:
        Нет.

    Возвращает:
        None: ничего не возвращает, только печатает на экран.
    """
    for name in team:
        show_pokemon(name)


def find_pokemon():
    """
    Спрашивает имя покемона и печатает его подробную информацию.

    Аргументы:
        Нет. Имя вводится с клавиатуры через input().

    Возвращает:
        None: ничего не возвращает, только печатает на экран.
    """
    name = input("Имя покемона: ").lower()
    show_pokemon(name)


def battle():
    """
    Выбирает двух покемонов из команды и сравнивает их силу.

    Силой считается сумма всех базовых статов покемона.

    Аргументы:
        Нет. Номера покемонов вводятся с клавиатуры через input().

    Возвращает:
        None: ничего не возвращает, только печатает результат боя.
    """
    for number in range(len(team)):
        print(number + 1, team[number])
    first = team[int(input("Номер первого покемона: ")) - 1]
    second = team[int(input("Номер второго покемона: ")) - 1]

    power1 = sum(s["base_stat"] for s in get_data(first)["stats"])
    power2 = sum(s["base_stat"] for s in get_data(second)["stats"])
    print(first, power1, "против", second, power2)
    if power1 > power2:
        print("Победил", first)
    elif power2 > power1:
        print("Победил", second)
    else:
        print("Ничья")


while True:
    print("\n1 - добавить, 2 - удалить, 3 - вся команда, 4 - найти, 5 - бой, 0 - выход")
    choice = input("Выбор: ")
    if choice == "1":
        add_pokemon()
    elif choice == "2":
        remove_pokemon()
    elif choice == "3":
        show_team()
    elif choice == "4":
        find_pokemon()
    elif choice == "5":
        battle()
    elif choice == "0":
        break
