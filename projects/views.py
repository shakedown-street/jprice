from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Project


def index(request):
    title = "Projects | Jordan Price"
    description = "Explore a selection of projects developed by Jordan Price."

    if not request.user.is_staff:
        projects = Project.objects.published()
    else:
        projects = Project.objects.all()

    context = {
        "title": title,
        "description": description,
        "projects": projects,
    }
    return render(request, "projects/index.html", context)


def detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    testimonials = project.testimonials.published()

    if not request.user.is_staff and not project.is_published:
        raise Http404("No Project matches the given query.")

    title = f"{project.name} | Jordan Price"
    description = project.description

    context = {
        "title": title,
        "description": description,
        "project": project,
        "testimonials": testimonials,
    }
    return render(request, "projects/detail.html", context)
