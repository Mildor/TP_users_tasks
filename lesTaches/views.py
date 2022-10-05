from django.forms import ModelForm, DateInput
from django.shortcuts import render, redirect
from django.utils.html import format_html
from lesTaches.forms import TaskForm, UserForm
from lesTaches.models import Task, User
from django import forms
from django.contrib import messages


# Create your views here.
def task_nav(request):
    return render(request, template_name='nav_task.html')


def task_listing(request, param=''):
    objects = Task.objects.all().order_by("name")
    user = ''
    if param != '':
        user = User.objects.get(id=param)
        objects = Task.objects.all().filter(owner=user)

    return render(request, template_name="liste.html", context={'taches': objects, 'user': user})


def user_choice(request):
    objects = User.objects.all()
    return render(request, template_name='all_users.html', context={'users': objects})


def task_details(request, param=''):
    objects = Task.objects.get(id=param)
    return render(request, template_name="detail.html", context={'tache': objects})


def task_form(request, param=''):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            messages.success(request, "Nouvelle Tâches : " + new_task.name)
            context = {"tache": new_task}
            return render(request, "detail.html", context)
    if param != '':
        user = User.objects.get(id=param)
        form = TaskForm(initial={'owner': user})

    return render(request, "taskForm.html", {"form": form})


def task_edit(request, param=''):
    data = Task.objects.get(id=param)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=data)
        if form.is_valid():
            new_task = form.save()
            messages.success(request, "Modification de la tache : " + new_task.name)
            context = {"tache": new_task}
            return render(request, "detail.html", context)
    else:
        form = TaskForm(instance=data)
    return render(request, 'edit_task.html', {'form': form, 'task': data})


def task_delete(request, param=''):
    task = Task.objects.get(id=param)
    task.delete()
    return render(request, 'del_task.html', {"deleted_task": task})


def user_form(request, lien=''):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Nouveau user : " + new_user.email)
            if lien == 'task':
                taskForm = TaskForm(initial={'owner': new_user})
                return render(request, "taskForm.html", {'form': taskForm})
            else:
                taches = Task.objects.all().filter(owner=new_user)
                context = {"user": new_user, "taches": taches}
                return render(request, "liste.html", context)
    context = {"form": form, "get": lien}
    return render(request, "userForm.html", context)


def user_edit(request, param=''):
    data = User.objects.get(id=param)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=data)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Modification du user : " + new_user.email)
            users = User.objects.all()
            return render(request, "all_users.html", {'users': users})
    else:
        form = UserForm(instance=data)
    return render(request, 'edit_user.html', {'form': form, 'user': data})


def user_delete(request, param=''):
    user = User.objects.get(id=param)
    user.delete()
    return render(request, 'del_user.html', {"deleted_user": user})
