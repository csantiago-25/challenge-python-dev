from django.urls import path
from .views import TaskListCreateAPI, TaskRetrieveUpdateDeleteAPI

urlpatterns = [
    path('tasks/', TaskListCreateAPI.as_view(), name='api_task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteAPI.as_view(), name='api_task_rud'),
]
