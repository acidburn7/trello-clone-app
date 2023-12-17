from django.contrib import admin
from django.urls import path
from .views import index, create, delete

urlpatterns = [
    path('', index, name='index'),
    path('<int:column_id>/create/', create, name='create'),
    path('<int:task_id>/delete/', delete, name='delete')
]
