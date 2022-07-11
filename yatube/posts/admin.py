from re import search
from django.contrib import admin
from .models import Group, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        )
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    # При регистрации модели Post источником конфигурации для неё назначаем 
    # класс PostAdmin
    list_editable = ('group',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
