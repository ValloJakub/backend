from django.db import models
from users.models import CustomUser
from Articles.models import Article


class FavouriteArticle(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')

    def __str__(self):
        return f"{self.user.email} - {self.article.title}"
