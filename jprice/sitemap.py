from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from blog.models import Post
from projects.models import Project


class StaticSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return [
            "index",
            "blog:index",
            "contact:index",
            "projects:index",
        ]

    def location(self, obj):
        return reverse(obj)


class BlogSitemap(Sitemap):
    changefreq = "yearly"

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("blog:detail", kwargs={"slug": obj.slug})


class ProjectsSitemap(Sitemap):
    changefreq = "yearly"

    def items(self):
        return Project.objects.published()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("projects:detail", kwargs={"slug": obj.slug})


sitemaps = {
    "static": StaticSitemap,
    "blog": BlogSitemap,
    "projects": ProjectsSitemap,
}
