from django import forms
from django.contrib import admin

from utils.widgets import MarkdownEditor

from .models import Project, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ProjectAdminForm(forms.ModelForm):
    model = Project

    class Meta:
        fields = "__all__"
        widgets = {"content": MarkdownEditor()}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = (
        "name",
        "slug",
        "published_at",
        "is_featured",
    )
    list_filter = (
        "technologies",
        "type",
        "published_at",
        "is_featured",
    )
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
