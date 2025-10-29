from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import handle_contact_form


def index(request):
    form = handle_contact_form(request)

    if isinstance(form, HttpResponseRedirect):
        return form

    context = {
        "form": form,
    }

    return render(request, "contact/index.html", context)


def submitted(request):
    return render(request, "contact/submitted.html")
