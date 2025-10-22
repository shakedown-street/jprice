from django.shortcuts import render

from .models import Project


def index(request):
    projects = Project.objects.all()

    context = {
        "projects": projects,
    }
    return render(request, "projects/index.html", context)


def detail(request, project_slug):
    project = Project.objects.get(slug=project_slug)

    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)
