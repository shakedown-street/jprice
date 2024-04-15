from django import forms
from django.contrib import admin

from blog.widgets import MarkdownEditor
from projects.models import Project, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }


class ProjectAdminForm(forms.ModelForm):
    model = Project

    class Meta:
        fields = "__all__"
        widgets = {"description": MarkdownEditor()}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = [
        "name",
        "slug",
    ]
    list_filter = [
        "technologies",
    ]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }
