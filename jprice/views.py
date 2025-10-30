from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from blog.models import Post
from contact.forms import handle_contact_form
from projects.models import Project, Technology


def index(request):
    featured_projects = Project.objects.featured()
    latest_posts = Post.objects.published()[:3]
    technologies = Technology.objects.all()
    contact_form = handle_contact_form(request)

    if isinstance(contact_form, HttpResponseRedirect):
        return contact_form

    return render(
        request,
        "jprice/index.html",
        {
            "projects": featured_projects,
            "posts": latest_posts,
            "technologies": technologies,
            "contact_form": contact_form,
        },
    )


def styleguide(request):
    return render(request, "jprice/styleguide.html")
