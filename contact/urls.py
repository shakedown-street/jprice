from django.urls import path

from contact.views import index, submitted

app_name = "contact"
urlpatterns = [
    path("", index, name="index"),
    path("submitted/", submitted, name="submitted"),
]
