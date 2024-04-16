from django import forms
from django.db.models import Count

from blog.models import Topic


class BlogSearchForm(forms.Form):
    search = forms.CharField(
        max_length=256,
        required=False,
        widget=forms.TextInput(attrs={"class": "jp-input"}),
    )
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.annotate(posts_count=Count("posts")).filter(
            posts_count__gt=0
        ),
        required=False,
        widget=forms.Select(attrs={"class": "jp-input"}),
    )
