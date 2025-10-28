from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Project


class ProjectsIndexTests(TestCase):
    def test_index_no_projects(self):
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["projects"], [])

    def test_unpublished_project(self):
        Project.objects.create(
            name="Test Project",
            slug="test-project",
            description="Test Description",
            content="Test Content",
        )
        response = self.client.get(reverse("projects:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["projects"], [])

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
    def test_detail_project_does_not_exist(self):
        response = self.client.get(reverse("projects:detail", args=("test-project",)))

        self.assertEqual(response.status_code, 404)

    def test_unpublished_detail(self):
        project = Project.objects.create(
            name="Test Project",
            slug="test-project",
            description="Test Description",
            content="Test Content",
        )
        response = self.client.get(reverse("projects:detail", args=(project.slug,)))

        self.assertEqual(response.status_code, 404)

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
