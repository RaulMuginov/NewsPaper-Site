from django.contrib import admin
from .models import NewsCategory, CartModel, News


# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(CartModel)
admin.site.register(News)

