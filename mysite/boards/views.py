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


def create_task(request, column_id):
    Task.objects.create(title=request.POST["title"], description="", column_id=column_id)
    return redirect('index')


def create_column(request, board_id):
    Column.objects.create(name=request.POST["name"], board_id=board_id)
    return redirect('index')


def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('index')


def delete_column(request, column_id):
    Column.objects.get(id=column_id).delete()
    return redirect('index')

def delete_board(request, board_id):
    return redirect('index')

def create_board(request):
    Task.objects.create(title=request.POST["title"])

    return redirect('index')
