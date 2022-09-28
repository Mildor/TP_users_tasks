from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.task_nav, name='crud_task'),
    path('listing/', views.task_listing, name='crud_task'),
    path('users/', views.user_choice, name='user_choice'),
    path('user_task/<param>/', views.task_listing_by_user, name='userTask'),
    path('detail/<param>/', views.task_details, name='details'),
    path('addTask/', views.task_form, name='TaskForm'),
    path('EditTask/<param>/', views.task_edit, name='TaskForm'),
    path('DeleteTask/<param>/', views.task_delete, name='TaskForm')
]