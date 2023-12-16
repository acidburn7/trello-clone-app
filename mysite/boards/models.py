from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=250)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    column = models.ForeignKey(Column, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
