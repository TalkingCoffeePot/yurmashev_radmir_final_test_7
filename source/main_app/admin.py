from django.contrib import admin
from main_app.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'task_status', 'date', 'details']
    list_editable = ['description', 'task_status', 'date', 'details']


admin.site.register(Task, TaskAdmin)