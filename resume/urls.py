from django.urls import path

from .views import resume_pdf

app_name = "resume"
urlpatterns = [
    path("", resume_pdf, name="resume_pdf"),
]
