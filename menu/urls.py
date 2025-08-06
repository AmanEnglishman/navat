from django.urls import path

from .views import DishListAPIView, DishDetailAPIView, DishCreateAPIView, DishUpdateAPIView, DishDeleteAPIView, \
    AddReviewToDishView

urlpatterns = [
    path('', DishListAPIView.as_view(), name='dish-list'),
    path('<int:pk>/', DishDetailAPIView.as_view(), name='dish-detail'),
    path('create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('update/<int:pk>/', DishUpdateAPIView.as_view(), name='dish-update'),
    path('delete/<int:pk>/', DishDeleteAPIView.as_view(), name='dish-delete'),
    path('<int:pk>/review/', AddReviewToDishView.as_view(), name='review-create'),
]
