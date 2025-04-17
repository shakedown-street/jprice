from django.urls import path

from resume.views import new_resume_pdf, resume_pdf

app_name = "resume"
urlpatterns = [
    path("", resume_pdf, name="resume_pdf"),
    path("new/", new_resume_pdf, name="new_resume_pdf"),
]
