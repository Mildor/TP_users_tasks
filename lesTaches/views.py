from django.forms import ModelForm, DateInput, EmailInput
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from lesTaches.models import Task, User
from django import forms
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def task_listing(request):
    objects = Task.objects.all().order_by("due_date")
    return render(request, template_name="liste.html", context={'taches': objects})


def task_details(request, param=''):
    objects = Task.objects.get(id=param)
    return render(request, template_name="detail.html", context={'tache': objects})


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nom"
        self.fields["description"].label = "description"
        self.fields["due_date"].label = "due_date"
        self.fields["schedule_date"].label = "schedule_date"
        owner = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ("name", "description", "due_date", "schedule_date", "owner")
        widgets = {
            "due_date": DateInput(),
            "schedule_date": DateInput(),
        }


def task_form(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            messages.success(request, "Nouvelle Tâches : " + new_task.name)
            context = {"tache": new_task}
            return render(request, "detail.html", context)
    context = {"form": form}
    return render(request, "taskForm.html", context)


def task_edit(request, param=''):
    data = Task.objects.get(id=param)
    if request.method == 'POST':

        form = TaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/lesTaches/')
    else:
        form = TaskForm(instance=data)
    return render(request, 'edit_task.html', {'form': form, 'task': data})


def task_delete(request, param=''):
    task = Task.objects.get(id=param)
    task.delete()
    return redirect('/lesTaches/')
