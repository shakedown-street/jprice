from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from contact.forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contact:submitted"))
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, "contact/index.html", context)


def submitted(request):
    return render(request, "contact/submitted.html")
