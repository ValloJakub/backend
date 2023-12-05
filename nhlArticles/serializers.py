# nhlProject/nhlArticles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'image')

    def validate_title(self, value):
        max_length = 255
        if len(value) > max_length:
            raise serializers.ValidationError(f'The title must be at most {max_length} characters long.')
        return value

    def validate_image(self, value):
        if not value:
            raise serializers.ValidationError('An image must be provided.')
        return value

    def create(self, validated_data):
        if 'title' in validated_data and 'image' in validated_data:
            return Article.objects.create(**validated_data)
        else:
            raise serializers.ValidationError('Both title and image are required fields.')
