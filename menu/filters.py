import django_filters

from menu.models import Dish


class DishFilters(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    weight_min = django_filters.NumberFilter(field_name='weight', lookup_expr='gte')
    weight_max = django_filters.NumberFilter(field_name='weight', lookup_expr='lte')

    class Meta:
        model = Dish
        fields = ['category', 'price_min', 'price_max', 'weight_min', 'weight_max']


