from django.shortcuts import render

# Create your views here.


def about(request):
    """Отображает статическую страницу «О проекте».

    Args:
        request (HttpRequest): Объект входящего HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренная страница pages/about.html.
    """
    context = {}
    return render(request, "pages/about.html", context)


def rules(request):
    """Отображает статическую страницу с правилами проекта.

    Args:
        request (HttpRequest): Объект входящего HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренная страница pages/rules.html.
    """
    context = {}
    return render(request, "pages/rules.html", context)
