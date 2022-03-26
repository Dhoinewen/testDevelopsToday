from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=1024, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Comments(models.Model):
    content = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return self.author_name


