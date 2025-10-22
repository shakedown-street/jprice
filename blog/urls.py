from django.urls import path

from .views import detail, index

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("<str:post_slug>/", detail, name="detail"),
]
