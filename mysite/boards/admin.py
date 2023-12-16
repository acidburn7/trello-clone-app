from django.contrib import admin

from boards.models import Board, Column, Task

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)
