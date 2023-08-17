from django.http import Http404
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Topic


def index(request):
    search_param = request.GET.get("search", "")
    topic_param = request.GET.get("topic", "")

    topics = Topic.objects.annotate(posts_count=Count("posts")).filter(
        posts_count__gt=0
    )
    posts = Post.objects.filter(
        published_at__isnull=False, published_at__lte=timezone.now()
    )

    if search_param:
        posts = posts.filter(title__icontains=search_param)
    if topic_param:
        posts = posts.filter(topics__slug=topic_param)

    context = {
        "topics": topics.order_by("name"),
        "posts": posts.order_by("-published_at"),
        "search_param": search_param,
        "topic_param": topic_param,
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
