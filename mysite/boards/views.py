from django.shortcuts import render
from django.http import HttpResponse

from .models import Board, Column, Task

def index(request):
    board = Board.objects.get(name="Проект трелло")
    context = {
        "board": board
    }

    return render(request, "boards/index.html", context)
