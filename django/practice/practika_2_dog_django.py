import json
import urllib.request
from wsgiref.simple_server import make_server

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="secret",
    ROOT_URLCONF=__name__,
    TEMPLATES=[{"BACKEND": "django.template.backends.django.DjangoTemplates"}],
)

import django  # noqa: E402

django.setup()

from django.core.wsgi import get_wsgi_application  # noqa: E402
from django.http import HttpResponse  # noqa: E402
from django.template import Context, Template  # noqa: E402
from django.urls import path  # noqa: E402


def get_data(url):
    """
    Отправляет GET-запрос по адресу и возвращает ответ как словарь.

    Аргументы:
        url (str): адрес, по которому нужно получить данные.

    Возвращает:
        dict: данные из ответа сервера, разобранные из JSON.
    """
    response = urllib.request.urlopen(url)
    return json.loads(response.read())


def get_breeds():
    """
    Возвращает список всех пород собак в алфавитном порядке.

    Аргументы:
        Нет.

    Возвращает:
        list[str]: названия пород, например ["affenpinscher", "african", ...].
    """
    data = get_data("https://dog.ceo/api/breeds/list/all")
    breeds = list(data["message"].keys())
    breeds.sort()
    return breeds


def get_image(breed):
    """
    Возвращает ссылку на одну случайную фотографию породы.

    Аргументы:
        breed (str): название породы, например "chow".

    Возвращает:
        str: ссылка на картинку.
    """
    data = get_data("https://dog.ceo/api/breed/" + breed + "/images/random")
    return data["message"]


# Шаблон Django: {{ значение }} выводит данные, {% for %} делает цикл
PAGE = Template("""
<h1>Собаки</h1>
<h2>Список пород</h2>
<ol>
{% for breed in breeds %}
  <li>{{ breed }}</li>
{% endfor %}
</ol>

<h2>Фотографии</h2>
<form method="get" action="/">
  <input type="text" name="breeds" value="{{ text }}">
  <button type="submit">Показать</button>
</form>

{% for item in photos %}
  <p>{{ item.breed }}</p>
  <img src="{{ item.image }}" width="300">
{% endfor %}
""")


def index(request):
    """
    Обрабатывает открытие главной страницы и отдаёт готовый HTML.

    Аргументы:
        request (django.http.HttpRequest): запрос от браузера.
            Поле breeds из формы берётся из request.GET.

    Возвращает:
        django.http.HttpResponse: страница со списком пород и фото.
    """
    text = request.GET.get("breeds", "")
    photos = []
    for breed in text.split(","):
        breed = breed.strip()
        if breed != "":
            photos.append({"breed": breed, "image": get_image(breed)})

    html = PAGE.render(Context({"breeds": get_breeds(), "text": text, "photos": photos}))
    return HttpResponse(html)


urlpatterns = [
    path("", index),
]


if __name__ == "__main__":
    server = make_server("127.0.0.1", 8080, get_wsgi_application())
    print("Открой http://127.0.0.1:8080/")
    server.serve_forever()
