from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    description = models.TextField()
    task_list = models.ForeignKey(List, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description
