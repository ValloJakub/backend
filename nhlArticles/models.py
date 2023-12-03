# nhlProject/nhlArticles/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
