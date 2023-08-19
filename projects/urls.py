from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:project_slug>/", views.detail, name="detail"),
]
