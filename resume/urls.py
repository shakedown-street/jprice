from django.urls import path

from resume.views import new_resume_pdf, resume_pdf, comprehensive_resume_pdf

app_name = "resume"
urlpatterns = [
    path("", resume_pdf, name="resume_pdf"),
    path("new/", new_resume_pdf, name="new_resume_pdf"),
    path("comprehensive/", comprehensive_resume_pdf, name="comprehensive_resume_pdf"),
]
