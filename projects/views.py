from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Project


def index(request):
    projects = Project.objects.filter(
        published_at__isnull=False,
        published_at__lte=timezone.now(),
    )

    context = {
        "projects": projects,
    }
    return render(request, "projects/index.html", context)


def detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    if not project.published_at or project.published_at > timezone.now():
        raise Http404("No Project matches the given query.")

    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)
