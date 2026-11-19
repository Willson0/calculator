# Здесь можно зарегистрировать модели в панели администратора.
from django.contrib import admin

from .models import Category, Location, Post

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
