from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    weight = models.FloatField()
    composition = models.TextField()
    image = models.ImageField(upload_to='dish_images')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Review(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Блюдо")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    comment = models.TextField(verbose_name='Комментарий')
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.dish.name} {self.name}'
