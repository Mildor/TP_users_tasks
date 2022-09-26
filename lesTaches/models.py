from django.db import models
from django.utils.html import format_html
import datetime



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
    due_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=7))
    schedule_date = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    def colored_due_date(self):
        if self.due_date - datetime.timedelta(days=7) > datetime.date.today():
            color = "green"
        elif self.due_date < datetime.date.today():
            color = "red"
        else:
            color = "orange"
        return format_html("<span style=color:%s>%s</span>" % (color, self.due_date))
