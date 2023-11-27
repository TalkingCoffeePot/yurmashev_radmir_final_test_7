from django.contrib import admin
from main_app.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'task_status', 'date']


admin.site.register(Task, TaskAdmin)