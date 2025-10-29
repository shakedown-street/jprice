from django import forms
from django.contrib import admin

from utils.widgets import MarkdownEditor

from .models import Post, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class PostAdminForm(forms.ModelForm):
    model = Post

    class Meta:
        fields = "__all__"
        widgets = {"content": MarkdownEditor()}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = (
        "title",
        "slug",
        "published_at",
    )
    list_filter = (
        "topics",
        "published_at",
    )
    search_fields = (
        "title",
        "content",
    )
    prepopulated_fields = {"slug": ("title",)}
