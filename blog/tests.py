from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Post

User = get_user_model()


class BlogIndexTests(TestCase):
    def _create_staff_user(self):
        return User.objects.create_user(
            username="staffuser",
            password="password",
            is_staff=True,
        )

    def test_index_no_posts(self):
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post matches the given query.")
        self.assertQuerySetEqual(response.context["posts"], [])

    def test_unpublished_post(self):
        # Regular user should not see unpublished posts
        Post.objects.create(title="Test Post", slug="test-post", content="Test Content")
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post matches the given query.")
        self.assertQuerySetEqual(response.context["posts"], [])

        # Staff user should see unpublished posts
        self.client.force_login(
            self._create_staff_user(),
        )
        response = self.client.get(reverse("blog:index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)

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
        self.assertQuerySetEqual(response.context["posts"], [post])


class BlogDetailTests(TestCase):
    def _create_staff_user(self):
        return User.objects.create_user(
            username="staffuser",
            password="password",
            is_staff=True,
        )

    def test_detail_post_does_not_exist(self):
        response = self.client.get(reverse("blog:detail", args=("test-post",)))

        self.assertEqual(response.status_code, 404)

    def test_unpublished_detail(self):
        # Regular user should get 404 for unpublished post
        post = Post.objects.create(
            title="Test Post", slug="test-post", content="Test Content"
        )
        response = self.client.get(reverse("blog:detail", args=(post.slug,)))

        self.assertEqual(response.status_code, 404)

        # Staff user should see unpublished project
        self.client.force_login(
            self._create_staff_user(),
        )
        response = self.client.get(reverse("blog:detail", args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["post"], post)

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
