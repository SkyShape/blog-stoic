from django.db import models
from post.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=800)
    like_count = models.IntegerField
    display_count = models.IntegerField

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment}'
