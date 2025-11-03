from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import handle_contact_form


def index(request):
    title = "Contact | Jordan Price"
    description = "Get in touch with Jordan Price for inquiries or feedback."

    form = handle_contact_form(request)

    if isinstance(form, HttpResponseRedirect):
        return form

    context = {
        "title": title,
        "description": description,
        "form": form,
    }

    return render(request, "contact/index.html", context)


def submitted(request):
    title = "Thank You! | Jordan Price"
    description = (
        "Thank you for reaching out to Jordan Price. Your message has been received."
    )

    context = {
        "title": title,
        "description": description,
    }

    return render(request, "contact/submitted.html", context)
