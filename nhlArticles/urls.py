# nhlProject/nhlProject/urls.py
from django.contrib import admin
from django.urls import path, include

from nhlArticles.views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-retrieve-update-destroy'),
]