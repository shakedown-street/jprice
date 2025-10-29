from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )


def handle_contact_form(request) -> ContactForm | HttpResponseRedirect:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contact:submitted"))
    else:
        form = ContactForm()
    return form
