from django.db import models

from jprice.mixins import TimestampMixin


class Contact(TimestampMixin):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField(max_length=1024)

    def __str__(self):
        return f"{self.name}"
