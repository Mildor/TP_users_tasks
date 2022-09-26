from django.contrib import admin

from lesTaches.models import Task, User


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date', 'schedule_date', 'due_date', 'owner')


class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Task, TaskAdmin)
admin.site.register(User, UserAdmin)
