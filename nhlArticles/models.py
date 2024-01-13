# nhlProject/nhlArticles/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.title
