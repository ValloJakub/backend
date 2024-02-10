from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FavouriteArticle
from .serializers import FavouriteArticleSerializer


class FavoriteArticleListAPIView(APIView):
    def get(self, request):
        favorite_articles = FavouriteArticle.objects.all()
        serializer = FavouriteArticleSerializer(favorite_articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavouriteArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteArticleDetailAPIView(APIView):
    def get(self, request, pk):
        favorite_article = get_object_or_404(FavouriteArticle, pk=pk)
        serializer = FavouriteArticleSerializer(favorite_article)
        return Response(serializer.data)

    def put(self, request, pk):
        favorite_article = get_object_or_404(FavouriteArticle, pk=pk)
        serializer = FavouriteArticleSerializer(favorite_article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        favorite_article = get_object_or_404(FavouriteArticle, pk=pk)
        serializer = FavouriteArticleSerializer(favorite_article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        favorite_article = get_object_or_404(FavouriteArticle, pk=pk)
        favorite_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
