from rest_framework import serializers

from .models import Cart, CartItem
from menu.models import Dish


class DishSerializerForCart(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'price', 'image', 'name')


class CartItemSerializer(serializers.ModelSerializer):
    dish = DishSerializerForCart(read_only=True)
    dish_id = serializers.PrimaryKeyRelatedField(
        queryset=Dish.objects.all(),
        source='dish',
        write_only=True
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'dish', 'dish_id', 'total_price')

    def get_total_price(self, obj):
        # Убедиться, что `obj` это экземпляр модели
        if isinstance(obj, CartItem):
            return obj.total_price()

        raise ValueError("Объект должен быть экземпляром модели CartItem")


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'items', 'total_price')

    def get_total_price(self, obj):
        return obj.total_price()
