from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.task_listing, name='crud_task'),
    path('detail/<param>/', views.task_details, name='details'),
    path('addTask/', views.task_form, name='TaskForm'),
    path('EditTask/<param>/', views.task_edit, name='TaskForm'),
    path('DeleteTask/<param>/', views.task_delete, name='TaskForm')
]