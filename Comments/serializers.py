from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'author', 'article']

    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("The content of the comment cannot be longer than 1000 characters.")
        return value


    def validate_author(self, value):
        if not value or not value.pk:
            raise serializers.ValidationError("Author is invalid or does not exists!.")
        return value