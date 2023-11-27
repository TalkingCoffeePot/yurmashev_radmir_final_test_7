from django.shortcuts import render
from main_app.models import Task, status_choices
# Create your views here.


def main_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    print(type(tasks))
    return render(request, 'main_page.html', context)

def new_task(request):
    context = {
        'status_choices': status_choices
    }
    return render(request, 'add_task.html', context)