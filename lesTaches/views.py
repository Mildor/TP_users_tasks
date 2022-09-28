from django.forms import ModelForm, DateInput
from django.shortcuts import render, redirect
from lesTaches.forms import TaskForm, UserForm
from lesTaches.models import Task, User
from django import forms
from django.contrib import messages


# Create your views here.
def task_nav(request):
    return render(request, template_name='nav_task.html')


def task_listing(request):
    objects = Task.objects.all().order_by("due_date")
    return render(request, template_name="liste.html", context={'taches': objects})


def user_choice(request):
    objects = User.objects.all()
    return render(request, template_name='all_users.html', context={'users': objects})


def task_listing_by_user(request, param=''):
    user = User.objects.get(id=param)
    objects = Task.objects.all().filter(owner=param)
    return render(request, template_name='user_task.html', context={'tasks': objects, 'user': user})


def task_details(request, param=''):
    objects = Task.objects.get(id=param)
    return render(request, template_name="detail.html", context={'tache': objects})


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


def user_form(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Nouveau user : " + new_user.email)
            context = {"user": new_user}
            return render(request, "user_task.html", context)
    context = {"form":form}
    return render(request, "userForm.html", context)


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
