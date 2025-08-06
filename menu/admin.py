from .models import Dish, Category, Review
from django.contrib import admin

@admin.register(Dish)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass