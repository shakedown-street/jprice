from django import forms
from django.contrib import admin

from .models import Post, Topic
from .widgets import MarkdownEditor


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }


class PostAdminForm(forms.ModelForm):
    model = Post

    class Meta:
        fields = "__all__"
        widgets = {"content": MarkdownEditor()}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        "title",
        "created_at",
        "updated_at",
        "published_at",
    ]
    list_filter = [
        "created_at",
        "updated_at",
        "topics",
    ]
    search_fields = [
        "title",
        "content",
    ]
    prepopulated_fields = {
        "slug": [
            "title",
        ]
    }
