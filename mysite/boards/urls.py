from django.contrib import admin
from django.urls import path
from .views import index, create_column, create_task, delete

urlpatterns = [
    path('', index, name='index'),
    path('<int:board_id>/create-column/', create_column, name='create-column'),
    path('<int:column_id>/create-task/', create_task, name='create-task'),
    path('<int:task_id>/delete/', delete, name='delete')
]
