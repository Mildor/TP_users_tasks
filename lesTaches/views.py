from django.http import HttpResponse
from django.shortcuts import render

from lesTaches.models import Task


# Create your views here.
def task_listing(request):
    objects = Task.objects.all().order_by("due_date")
    return render(request, template_name="liste.html", context={'taches':objects})