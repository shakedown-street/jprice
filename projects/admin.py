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
        "created_at",
        "updated_at",
        "published_at",
    )
    list_filter = ("technologies",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
