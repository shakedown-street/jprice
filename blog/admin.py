from django.contrib import admin

from .models import Post, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "updated_at",
        "published_at",
    ]
    list_filter = [
        "created_at",
        "updated_at",
        "topics",
    ]
    search_fields = [
        "title",
        "content",
    ]
    prepopulated_fields = {
        "slug": [
            "title",
        ]
    }
