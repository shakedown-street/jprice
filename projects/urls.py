from django.urls import path

from .views import detail, index

app_name = "projects"
urlpatterns = [
    path("", index, name="index"),
    path("<str:project_slug>/", detail, name="detail"),
]
