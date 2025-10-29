from django.urls import path

from .views import detail, index

app_name = "projects"
urlpatterns = [
    path("", index, name="index"),
    path("<str:slug>/", detail, name="detail"),
]
