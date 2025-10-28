from django.db import models

from jprice.mixins import TimestampMixin


class Technology(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "technology"
        verbose_name_plural = "technologies"

    def __str__(self):
        return self.name


class Project(TimestampMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=512)
    content = models.TextField()
    technologies = models.ManyToManyField(
        Technology, blank=True, related_name="projects"
    )
    github_url = models.URLField(max_length=255, blank=True)
    website_url = models.URLField(max_length=255, blank=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
