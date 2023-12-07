from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main_app.models import Task, status_choices
from main_app.forms import TaskForm
# Create your views here.


def main_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'main_page.html', context)

#############################################################################
def new_task(request):
    context = {
        'status_choices': status_choices
    }
    return render(request, 'add_task.html', context)

#############################################################################
def add_task(request):
    if request.method == 'GET':
        form = TaskForm()
        context = {
        'form': form
        }
        return render(request, 'add_task.html', context)
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(description=form.cleaned_data['description'], 
                                task_status=form.cleaned_data['task_status'], 
                                date=form.cleaned_data['date'], 
                                details=form.cleaned_data['details'])
            
            return redirect('task_details', pk=task.pk)
        else:
            return render(request, 'new_task', context={'form': form})

##############################################################################
def detailed_view(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task': task
    }
    return render(request, 'detailed_task.html', context)
