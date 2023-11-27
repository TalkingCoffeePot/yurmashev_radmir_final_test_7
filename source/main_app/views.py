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

def add_task(request):
    description = request.POST.get('description')
    
    status = request.POST.get('status')
    for x in status_choices:
        if x[0] == status:
            status = x[1]

    date = request.POST.get('date')

    Task.objects.create(description=description, task_status=status, date=date)
    task = Task.objects.all()

    context = {
        'tasks': task
    }
    return render(request, 'main_page.html', context)
