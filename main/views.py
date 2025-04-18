from django.shortcuts import render , redirect
from django.views.generic import View
from .models import Tasks
from django.contrib import messages



class AdminDashboardView(View):
    def get(self, request):
        return render(request, 'index.html')

def add_task(request):
    tasks = Tasks.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        temps =Tasks.objects.create(title=title)
        if temps:
            messages.success(request , 'Todo added successfully')
            return render(request , 'index.html', context={'tasks':tasks})
        else:
            messages.error(request , 'Something went wrong')
            return render(request , 'index.html', context={'tasks':tasks})
    return render(request, 'index.html', context= {'tasks': tasks})

def update_status(request, task_id, status):
    task = Tasks.objects.get(id = task_id)
    task.status = status
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))

def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER'))
    