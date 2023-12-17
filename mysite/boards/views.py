from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from .models import Board, Column, Task

def index(request):
    board = Board.objects.get(name="Проект трелло")
    columns = Column.objects.filter(board=board)
    tasks = Task.objects.filter(column_id__in=columns.values_list("id"))

    context = {
        "board": board,
        "columns": columns,
        "tasks": tasks,
    }
    return render(request, "boards/index.html", context)

def create(request, column_id):
    Task.objects.create(title=request.POST["title"], description=request.POST["description"], column_id=column_id)
    return redirect('index')

def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('index')
