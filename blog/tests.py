from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Post


class BlogIndexTests(TestCase):
    def test_index_no_posts(self):
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post matches the given query.")
        self.assertQuerysetEqual(response.context["posts"], [])

    def test_unpublished_post(self):
        Post.objects.create(title="Test Post", slug="test-post", content="Test Content")
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post matches the given query.")
        self.assertQuerysetEqual(response.context["posts"], [])

    def test_published_post(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Test Content",
            published_at=timezone.now(),
        )
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertQuerysetEqual(response.context["posts"], [post])


class BlogDetailTests(TestCase):
    def test_detail_post_does_not_exist(self):
        response = self.client.get(reverse("blog:detail", args=("test-post",)))

        self.assertEqual(response.status_code, 404)

    def test_unpublished_detail(self):
        post = Post.objects.create(
            title="Test Post", slug="test-post", content="Test Content"
        )
        response = self.client.get(reverse("blog:detail", args=(post.slug,)))

        self.assertEqual(response.status_code, 404)

    def test_published_detail(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Test Content",
            published_at=timezone.now(),
        )
        response = self.client.get(reverse("blog:detail", args=(post.slug,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertEqual(response.context["post"], post)
