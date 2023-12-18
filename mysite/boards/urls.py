from django.contrib import admin
from django.urls import path
from .views import index, create_column, create_task, delete, delete_board, delete_column

urlpatterns = [
    path('', index, name='index'),
    path('<int:board_id>/create-column/', create_column, name='create-column'),
    path('<int:column_id>/create-task/', create_task, name='create-task'),
    path('<int:task_id>/delete/', delete, name='delete'),
    path('<int:board_id>/delete-board/', delete_board, name='delete-board'),
    path('<int:column_id>/delete-column/', delete_column, name='delete-column')
]
