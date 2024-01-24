import base64

from django.db import models

from users.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField(blank=True, null=True)  # reprezentovaný v base64
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def set_image_from_file(self, image_path):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                self.image = f"data:image/png;base64,{encoded_string}"
        except FileNotFoundError:
            pass

    def get_image(self):
        return self.image
