from rest_framework import serializers
import base64

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'category', 'title', 'description', 'image', 'created_at']

    def validate_title(self, value):
        if len(value) < 20 or len(value) > 100:
            raise serializers.ValidationError("Title must be between 20 and 100 characters.")
        return value

    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError("Category must be selected.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value

    def validate_image(self, value):
        if value is not None:
            try:
                # Odstráni predponu "data:image/png;base64," a dekóduje base64 reprezentáciu
                _, data = value.split(',', 1)
                decoded_image = base64.b64decode(data)
            except Exception as e:
                raise serializers.ValidationError("Invalid base64 image representation.")
        return value
