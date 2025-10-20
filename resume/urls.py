from django.urls import path

from resume.views import invoice_pdf, old_resume_pdf, resume_pdf

app_name = "resume"
urlpatterns = [
    path("", resume_pdf, name="resume_pdf"),
    path("old/", old_resume_pdf, name="old_resume_pdf"),
    path("invoice/", invoice_pdf, name="invoice_pdf"),
]
