from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Project


def index(request):
    if not request.user.is_staff:
        projects = Project.objects.published()
    else:
        projects = Project.objects.all()

    context = {
        "projects": projects,
    }
    return render(request, "projects/index.html", context)


def detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    if not request.user.is_staff and not project.is_published:
        raise Http404("No Project matches the given query.")

    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)
