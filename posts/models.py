from django.db import models
from django.contrib.auth import get_user_model


# Get the User Model
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    body = models.TextField(blank=True)

    published_at = models.DateTimeField(auto_now_add=True)