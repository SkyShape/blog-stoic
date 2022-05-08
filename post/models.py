from django.db import models
from ckeditor.fields import RichTextField


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): return self.name


class Post(models.Model):
    # user = 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    # description = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.title
