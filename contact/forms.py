from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Contact


class ContactForm(forms.ModelForm):
    # Honeypot field
    website_url = forms.CharField(required=False, widget=forms.HiddenInput)
    captcha = CaptchaField(
        help_text="Please complete the CAPTCHA to prove you're human.",
        widget=CaptchaTextInput(attrs={"class": "fluid"}),
    )

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
            "message": forms.Textarea(attrs={"class": "resize-y fluid"}),
        }

    def clean_website_url(self):
        # Reject submissions where the honeypot field is filled out
        value = self.cleaned_data.get("website_url")

        if value:
            raise forms.ValidationError("Bot detected.")

        return value


def handle_contact_form(request) -> ContactForm | HttpResponseRedirect:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contact:submitted"))
    else:
        form = ContactForm()
    return form
