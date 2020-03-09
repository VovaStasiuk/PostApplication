from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.likes.models import Like


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=150)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
