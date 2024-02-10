from rest_framework import serializers
from .models import FavouriteArticle

class FavouriteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteArticle
        fields = ['id', 'user', 'article', 'created_at']

    def validate(self, data):
        user = data['user']
        article = data['article']

        if FavouriteArticle.objects.filter(user=user, article=article).exists():
            raise serializers.ValidationError("This article is already in the user's favorites.")

        return data
