from django.urls import path

from . import views

app_name = "resume"
urlpatterns = [
    path("", views.resume_pdf, name="resume_pdf"),
]
