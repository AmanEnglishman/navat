from rest_framework import serializers

from .models import Dish, Review, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name')


class DishSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'image', 'category')


class DishDetailSerializer(serializers.ModelSerializer):
    similar_dishes = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'is_available', 'composition', 'weight', 'image', 'similar_dishes')

    def get_similar_dishes(self, obj):
        queryset = Dish.objects.filter(category=obj.category).exclude(id=obj.id)[:5]
        return DishSimpleSerializer(queryset, many=True).data


class DishSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'image',)


class ReviewForDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'email', 'comment', 'user')


class DishCreateSerializer(serializers.ModelSerializer):
    # Для записи принимаем только ID категории
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'image', 'category')

