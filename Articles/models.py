from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    specification = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
