from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    """Абстрактная модель с полями, которые есть у всех моделей блога.

    Attributes:
        is_published: Виден ли объект на сайте.
        created_at: Дата и время, когда объект добавили.
    """

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        abstract = True


class Category(BaseModel):
    """Категория, к которой относятся публикации.

    Attributes:
        title: Заголовок категории.
        description: Описание категории.
        slug: Идентификатор для адреса страницы, уникальный.
        is_published: Виден ли категория на сайте.
        created_at: Дата и время, когда категорию добавили.
    """

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'
        ),
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BaseModel):
    """Географическая метка, которую можно указать у публикации.

    Attributes:
        name: Название места.
        is_published: Виден ли место на сайте.
        created_at: Дата и время, когда место добавили.
    """

    name = models.CharField(
        max_length=256,
        verbose_name='Название места',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(BaseModel):
    """Публикация, которую написал пользователь.

    Attributes:
        title: Заголовок публикации.
        text: Текст публикации.
        pub_date: Дата и время публикации. Может быть в будущем.
        author: Пользователь, который написал публикацию.
        location: Место, связанное с публикацией. Может быть пустым.
        category: Категория публикации. Может быть пустой.
        is_published: Виден ли публикация на сайте.
        created_at: Дата и время, когда публикацию добавили.
    """

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
