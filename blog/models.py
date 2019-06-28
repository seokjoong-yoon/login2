from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="")
    author = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:5]
        
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30, null=True, blank=True)
    
class Follow(models.Model):
    follow = models.BooleanField(default=False)

class Follow_post(models.Model):
    follow = models.ForeignKey('blog.Follow', on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=30, null=True, blank=True)
