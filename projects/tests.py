from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Project

User = get_user_model()


class ProjectsIndexTests(TestCase):
    def _create_staff_user(self):
        return User.objects.create_user(
            username="staffuser",
            password="password",
            is_staff=True,
        )

    def test_index_no_projects(self):
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["projects"], [])

    def test_unpublished_project(self):
        # Regular user should not see unpublished projects
        Project.objects.create(
            name="Test Project",
            slug="test-project",
            description="Test Description",
            content="Test Content",
        )
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["projects"], [])

        # Staff user should see unpublished projects

        self.client.force_login(
            self._create_staff_user(),
        )
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["projects"]), 1)

    def test_published_project(self):
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            description="Test Description",
            content="Test Content",
            published_at=timezone.now(),
        )
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, project.name)
        self.assertQuerySetEqual(response.context["projects"], [project])


class ProjectDetailTests(TestCase):
    def _create_staff_user(self):
        return User.objects.create_user(
            username="staffuser",
            password="password",
            is_staff=True,
        )

    def test_detail_project_does_not_exist(self):
        response = self.client.get(reverse("projects:detail", args=("test-project",)))

        self.assertEqual(response.status_code, 404)

    def test_unpublished_detail(self):
        # Regular user should get 404 for unpublished project
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            description="Test Description",
            content="Test Content",
        )
        response = self.client.get(reverse("projects:detail", args=(project.slug,)))

        self.assertEqual(response.status_code, 404)

        # Staff user should see unpublished project
        self.client.force_login(
            self._create_staff_user(),
        )
        response = self.client.get(reverse("projects:detail", args=(project.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["project"], project)

    def test_published_detail(self):
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            description="Test Description",
            content="Test Content",
            published_at=timezone.now(),
        )
        response = self.client.get(reverse("projects:detail", args=(project.slug,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, project.name)
        self.assertEqual(response.context["project"], project)
