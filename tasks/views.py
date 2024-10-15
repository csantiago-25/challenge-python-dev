# views.py (limpiado)

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from background_task import background
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .forms import TaskForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Listar tareas
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Crear tarea
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})

# Actualizar tarea
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {'form': form})

# Eliminar tarea
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# API Views
@permission_classes([IsAuthenticated])
class TaskListCreateAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@permission_classes([IsAuthenticated])
class TaskRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Definición de la tarea en segundo plano
@background(schedule=60)
def send_task_notification(email, title):
    print(f"Enviando notificación a {email} para la tarea {title}")
