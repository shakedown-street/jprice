from django.shortcuts import render

from blog.models import Post
from contact.forms import ContactForm
from projects.models import Project


def index(request):
    projects = Project.objects.all()[:3]
    posts = Post.objects.all()[:3]
    form = ContactForm()

    return render(
        request,
        "jprice/index.html",
        {
            "projects": projects,
            "posts": posts,
            "form": form,
        },
    )
