"""
URL configuration for jprice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .sitemap import sitemaps
from .views import index, styleguide

urlpatterns = [
    path("", index, name="index"),
    path("blog/", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path("projects/", include("projects.urls")),
    path("resume/", include("resume.urls")),
    path("styleguide/", styleguide),
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": sitemaps,
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
