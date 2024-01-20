# models.py
from django.db import models
from Articles.models import Article
from users.models import CustomUser

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    # výpis
    def __str__(self):
        return f"{self.author.username} - {self.created_at}: {self.content}"