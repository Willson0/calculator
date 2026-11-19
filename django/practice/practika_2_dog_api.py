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


def get_numbered_breeds():
    """
    Получает все породы собак и оформляет их как нумерованный список.

    Аргументы:
        Нет.

    Возвращает:
        list[str]: строки вида "1. affenpinscher", "2. african", ...
    """
    data = get_data("https://dog.ceo/api/breeds/list/all")
    breeds = sorted(data["message"].keys())
    numbered = []
    for number, breed in enumerate(breeds, start=1):
        numbered.append(str(number) + ". " + breed)
    return numbered


def get_dog_photos(breeds):
    """
    Печатает ссылку на одну случайную фотографию для каждой породы из списка.

    Аргументы:
        breeds (list[str]): названия пород, например ["african", "chow"].

    Возвращает:
        None: ничего не возвращает, только печатает ссылки на фото.
    """
    for breed in breeds:
        data = get_data("https://dog.ceo/api/breed/" + breed + "/images/random")
        print(breed, ":", data["message"])


def main():
    """
    Запускает программу: показывает список пород и печатает фото введённых пород.

    Аргументы:
        Нет. Породы вводятся с клавиатуры через input().

    Возвращает:
        None: ничего не возвращает, только печатает на экран.
    """
    for line in get_numbered_breeds():
        print(line)

    text = input("Введите породы через запятую: ")
    breeds = []
    for part in text.split(","):
        breeds.append(part.strip().lower())
    get_dog_photos(breeds)


main()
