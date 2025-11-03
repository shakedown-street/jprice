from django import forms
from django.db.models import Count, Q
from django.utils import timezone

from .models import Topic


class BlogSearchForm(forms.Form):
    template_name = "blog/partials/blog_search_form.html"

    search = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search"}),
    )
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.annotate(
            posts_count=Count(
                "posts",
                filter=(
                    Q(posts__published_at__isnull=False)
                    & Q(posts__published_at__lte=timezone.now())
                ),
            )
        ).filter(posts_count__gt=0),
        required=False,
    )
