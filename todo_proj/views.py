from django.shortcuts import render
from todo.models import Task



def home(request):
    tasks = Task.objects.filter(is_completed = False)
    done_task = Task.objects.filter(is_completed = True)
    context = {
        'tasks': tasks,
        'done_task':done_task,
    }
    return render(request , 'home.html', context)

