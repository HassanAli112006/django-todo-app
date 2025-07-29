from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Function to add a new task
def add_task(request):
    new_task = request.POST.get('entered_task')
    Task.objects.create(task = new_task)
    return redirect('home_page')


# Function to mark a task Done
def done(request, pk):
    task = get_object_or_404(Task , pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home_page')


# Function to mark a task Undone
def undone(request, pk):
    task = get_object_or_404(Task , pk = pk)
    task.is_completed = False
    task.save()
    return redirect('home_page')


# Function to edit a task
def edit(request, pk):
    task = get_object_or_404(Task, pk = pk)
    new_task = request.POST.get('updated_task')
    if request.method == 'POST':

        task.task = new_task
        task.save()
        return redirect('home_page')
    else:
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


# Function to delete tasks
def delete_task(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    return redirect('home_page')



