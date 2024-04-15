from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "jp-input"
        self.fields["last_name"].widget.attrs["class"] = "jp-input"
        self.fields["email"].widget.attrs["class"] = "jp-input"
        self.fields["subject"].widget.attrs["class"] = "jp-input"
        self.fields["message"].widget.attrs["class"] = "jp-input"

    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
        ]
