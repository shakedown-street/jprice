import os
from django.db import models


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


def project_image_upload_to(instance, filename):
    ext = os.path.splitext(filename)[-1]
    if filename == "blob":
        ext = ".png"
    return f"projects/{instance.slug}/image{ext}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=project_image_upload_to, blank=True)
    technologies = models.ManyToManyField(Technology)
    github_url = models.URLField(max_length=255, blank=True)
    website_url = models.URLField(max_length=255, blank=True)

    # TODO: Add a "published" field to the model and use it to filter
    #       projects in the view.
    # TODO: Add an ordering field to the model and use it to order
    #       projects in the view.

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name
