from blog.models import Category, Post
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


def get_published_posts():
    """Возвращает публикации, которые можно показывать на сайте.

    Публикация попадает в выборку, если её дата уже наступила,
    она опубликована и её категория тоже опубликована.

    Returns:
        QuerySet: Выборка опубликованных публикаций.
    """
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    """Показывает главную страницу с последними пятью публикациями.

    Args:
        request: Объект запроса от пользователя.

    Returns:
        HttpResponse: Страница blog/index.html со списком post_list.
    """
    post_list = (
        get_published_posts()
        .select_related('category', 'location', 'author')
        .order_by('-pub_date')[:5]
    )
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, id):
    """Показывает одну публикацию по её номеру.

    Если публикация недоступна для показа, возвращается ошибка 404.

    Args:
        request: Объект запроса от пользователя.
        id: Номер публикации в базе данных.

    Returns:
        HttpResponse: Страница blog/detail.html с публикацией post.

    Raises:
        Http404: Если публикации с таким номером нет или она недоступна.
    """
    post = get_object_or_404(get_published_posts(), id=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Показывает публикации одной категории.

    Если категории с таким идентификатором нет или она скрыта,
    возвращается ошибка 404.

    Args:
        request: Объект запроса от пользователя.
        category_slug: Идентификатор категории из адреса страницы.

    Returns:
        HttpResponse: Страница blog/category.html со списком post_list.

    Raises:
        Http404: Если категория не найдена или скрыта.
    """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = (
        get_published_posts()
        .filter(category=category)
        .order_by('-pub_date')
    )
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list},
    )
