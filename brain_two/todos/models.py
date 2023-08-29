from django.db import models
from django.utils import timezone

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
