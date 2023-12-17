from django.shortcuts import render
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

def create(request, board_id, column_id):
    Task.objects.create(title=request.POST["title"], description=request.POST["description"], column_id=column_id)
    
    board = Board.objects.get(name="Проект трелло")
    columns = Column.objects.filter(board=board)
    tasks = Task.objects.filter(column_id__in=columns.values_list("id"))

    context = {
        "board": board,
        "columns": columns,
        "tasks": tasks,
    }
    return render(request, "boards/index.html", context)

def delete(request, task_id):
    Task.objects.get(id=task_id).delete()

    board = Board.objects.get(name="Проект трелло")
    columns = Column.objects.filter(board=board)
    tasks = Task.objects.filter(column_id__in=columns.values_list("id"))

    context = {
        "board": board,
        "columns": columns,
        "tasks": tasks,
    }
    return render(request, "boards/index.html", context)
