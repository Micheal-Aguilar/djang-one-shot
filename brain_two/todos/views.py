from django.shortcuts import render
from .models import ToDoList

# Create your views here.


def todo_list(request):
    todo_list = ToDoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": todo_list})
