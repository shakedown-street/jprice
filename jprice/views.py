from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from blog.models import Post
from contact.forms import handle_contact_form
from projects.models import Project


def index(request):
    projects = Project.objects.filter(
        published_at__isnull=False,
        published_at__lte=timezone.now(),
    )[:3]
    posts = Post.objects.filter(
        published_at__isnull=False,
        published_at__lte=timezone.now(),
    )[:3]
    form = handle_contact_form(request)

    if isinstance(form, HttpResponseRedirect):
        return form

    return render(
        request,
        "jprice/index.html",
        {
            "projects": projects,
            "posts": posts,
            "form": form,
        },
    )


def poorman(request):
    return render(request, "jprice/poorman.html")
