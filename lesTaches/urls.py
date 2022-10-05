from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.task_nav, name='crud_task'),
    path('listing/', views.task_listing, name='listing_task'),
    path('listing/<param>/', views.task_listing, name='listing_task_users'),
    path('users/', views.user_choice, name='user_choice'),
    path('detail/<param>/', views.task_details, name='details'),
    path('addTask/', views.task_form, name='TaskForm'),
    path('addTask/<param>/', views.task_form, name='TaskForm_param'),
    path('EditTask/<param>/', views.task_edit, name='TaskForm-edit'),
    path('DeleteTask/<param>/', views.task_delete, name='TaskForm-delete'),
    path('addUser/', views.user_form, name='UserForm'),
    path('addUser/<lien>/', views.user_form, name='UserForm_param'),
    path('EditUser/<param>/', views.user_edit, name='UserForm-edit'),
    path('DeleteUser/<param>/', views.user_delete, name='UserForm-delete'),
]
