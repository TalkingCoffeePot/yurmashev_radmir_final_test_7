from django.shortcuts import render
from main_app.models import Task
# Create your views here.


def main_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    print(type(tasks))
    return render(request, 'main_page.html', context)