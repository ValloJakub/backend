from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'specification', 'title', 'description', 'image', 'created_at']

        def validate_title(self, value):
            if len(value) < 20 or len(value) > 100:
                raise serializers.ValidationError("Title must be between 20 and 100 characters.")
            return value

        def validate_specification(self, value):
            if not value:
                raise serializers.ValidationError("Specification must be selected.")
            return value

        def validate_description(self, value):
            if not value.strip():
                raise serializers.ValidationError("Description cannot be empty.")
            return value