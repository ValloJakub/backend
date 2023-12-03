# nhlProject/nhlArticles/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
