from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.text import Truncator

from utils.templatetags.markdown import unmark

from .forms import BlogSearchForm
from .models import Post


def index(request):
    title = "Blog | Jordan Price"
    description = "Read the latest articles and updates from Jordan Price."

    if not request.user.is_staff:
        posts = Post.objects.published()
    else:
        posts = Post.objects.all()

    form = BlogSearchForm(request.GET)

    if form.is_valid():
        search = form.cleaned_data.get("search")
        topic = form.cleaned_data.get("topic")

        if search:
            posts = posts.filter(title__icontains=search)

        if topic:
            posts = posts.filter(topics=topic)

    context = {
        "title": title,
        "description": description,
        "form": form,
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if not request.user.is_staff and not post.is_published:
        raise Http404("No Post matches the given query.")

    title = f"{post.title} | Jordan Price"
    raw_content = unmark.convert(post.content)
    description = Truncator(raw_content).words(30, truncate=" …")

    context = {
        "title": title,
        "description": description,
        "post": post,
    }

    return render(request, "blog/detail.html", context)
