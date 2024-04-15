from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Topic


def index(request):
    topics = Topic.objects.annotate(posts_count=Count("posts")).filter(
        posts_count__gt=0
    )
    posts = Post.objects.filter(
        published_at__isnull=False, published_at__lte=timezone.now()
    )

    if request.method == "POST":
        search = request.POST.get("search", None)
        topic = request.POST.get("topic", None)

        if search:
            posts = posts.filter(title__icontains=search)

        if topic:
            posts = posts.filter(topics__slug=topic)

        context = {
            "posts": posts.order_by("-published_at"),
        }

        return render(request, "blog/partials/posts.html", context)

    context = {
        "topics": topics.order_by("name"),
        "posts": posts.order_by("-published_at"),
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
