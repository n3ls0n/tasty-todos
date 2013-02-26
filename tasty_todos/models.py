from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    order = models.IntegerField(default=0)