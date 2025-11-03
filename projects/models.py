from django.db import models
from django.db.models.functions import Lower
from django.utils import timezone

from jprice.mixins import TimestampMixin


class Technology(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = (Lower("name"),)
        verbose_name = "technology"
        verbose_name_plural = "technologies"

    def __str__(self):
        return self.name


class ProjectManager(models.Manager):
    def published(self):
        return self.filter(
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )

    def featured(self):
        return self.published().filter(is_featured=True)


class Project(TimestampMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=512)
    technologies = models.ManyToManyField(
        Technology, blank=True, related_name="projects"
    )
    type = models.CharField(max_length=255, blank=True)
    github_url = models.URLField(max_length=255, blank=True)
    website_url = models.URLField(max_length=255, blank=True)
    content = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    objects = ProjectManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def is_published(self):
        return self.published_at is not None and self.published_at <= timezone.now()
