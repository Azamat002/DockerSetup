# blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(max_length=200, null=True)  # Allow null values

    def __str__(self):
        return self.title
