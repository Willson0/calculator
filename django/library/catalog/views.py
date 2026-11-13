from django.shortcuts import render


def book(request):
    """
    Показывает страницу одной книги.

    Аргументы:
        request (HttpRequest): запрос от браузера.

    Возвращает:
        HttpResponse: страница с данными книги из шаблона book_detail.html.
    """
    context = {
        "book":
        {
            "title": "Преступление и наказание",
            "author": "Достоевский",
            "year": 1823,
            "pages": 123,
            "rating": 4.3,
            "genres": ["роман", "классика", "психология"],
            "available": True,
            "price": 450,
        },
        "comments_count": 0,
    }
    return render(request, 'catalog/book_detail.html', context)


def book_list(request):
    """
    Показывает список книг.

    Аргументы:
        request (HttpRequest): запрос от браузера.

    Возвращает:
        HttpResponse: страница со списком книг из шаблона book_list.html.
    """
    books = [
        {"title": "Преступление и наказание", "author": "Достоевский", "price": 450},
        {"title": "Война и мир", "author": "Толстой", "price": 1200},
        {"title": "Мастер и Маргарита", "author": "Булгаков", "price": 890},
    ]
    return render(request, 'catalog/book_list.html', {"books": books})
