from django.db import models

from jprice.mixins import TimestampMixin


class Topic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Post(TimestampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    topics = models.ManyToManyField(Topic, blank=True, related_name="posts")
    content = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = (
            "-published_at",
            "title",
        )

    def __str__(self):
        return self.title
