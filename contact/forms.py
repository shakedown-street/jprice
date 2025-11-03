from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Contact


class ContactForm(forms.ModelForm):
    template_name = "contact/partials/contact_form.html"

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "fluid"}),
            "email": forms.EmailInput(attrs={"class": "fluid"}),
            "message": forms.Textarea(attrs={"class": "resize-y", "cols": 30}),
        }


def handle_contact_form(request) -> ContactForm | HttpResponseRedirect:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contact:submitted"))
    else:
        form = ContactForm()
    return form
