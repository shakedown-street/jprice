from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import BlogSearchForm
from .models import Post


def index(request):
    posts = Post.objects.filter(
        published_at__isnull=False,
        published_at__lte=timezone.now(),
    )

    form = BlogSearchForm(request.GET)

    if form.is_valid():
        search = form.cleaned_data.get("search")
        topic = form.cleaned_data.get("topic")

        if search:
            posts = posts.filter(title__icontains=search)

        if topic:
            posts = posts.filter(topics=topic)

    context = {
        "form": form,
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if not post.published_at or post.published_at > timezone.now():
        raise Http404("No Post matches the given query.")

    context = {
        "post": post,
    }

    return render(request, "blog/detail.html", context)
