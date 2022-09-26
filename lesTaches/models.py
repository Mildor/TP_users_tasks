import datetime as DT
from django.utils import timezone

from django.db import models


# Create your models here.

class User(models.Model):
    username = None
    email = models.EmailField('email adress', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    creation_date = models.DateField(auto_now=True)
    closed = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now)
    schedule_date = models.DateField(default=(timezone.now() + DT.timedelta(days=7)))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
