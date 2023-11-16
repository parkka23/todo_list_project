from django.utils import timezone

from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title
