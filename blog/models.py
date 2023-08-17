from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    topics = models.ManyToManyField(Topic, related_name="posts")

    class Meta:
        ordering = [
            "-published_at",
        ]

    def __str__(self):
        return self.title
