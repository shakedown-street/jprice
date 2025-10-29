from django.db import models
from django.db.models.functions import Lower
from django.utils import timezone

from jprice.mixins import TimestampMixin


class Topic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = (Lower("name"),)

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    def published(self):
        return self.filter(
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )


class Post(TimestampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    topics = models.ManyToManyField(Topic, blank=True, related_name="posts")
    content = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)

    objects = PostManager()

    class Meta:
        ordering = (
            "-published_at",
            "title",
        )

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.published_at is not None and self.published_at <= timezone.now()
