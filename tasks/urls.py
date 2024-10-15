# tasks/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # Rutas de la interfaz web
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),

    # Rutas de autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rutas de la API REST
    path('api/tasks/', views.TaskListCreateAPI.as_view(), name='task_list_create_api'),
    path('api/tasks/<int:pk>/', views.TaskRetrieveUpdateDeleteAPI.as_view(), name='task_detail_api'),
]
