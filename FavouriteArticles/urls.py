from django.urls import path
from .views import FavoriteArticleListAPIView, FavoriteArticleDetailAPIView

urlpatterns = [
    path('favorites/', FavoriteArticleListAPIView.as_view(), name='favorite_article_list'),
    path('favorites/<int:pk>/', FavoriteArticleDetailAPIView.as_view(), name='favorite_article_detail'),
]