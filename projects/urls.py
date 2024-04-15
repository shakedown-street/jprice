from django.urls import path

from projects.views import index, detail

app_name = "projects"
urlpatterns = [
    path("", index, name="index"),
    path("<str:project_slug>/", detail, name="detail"),
]
