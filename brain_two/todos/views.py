from django.shortcuts import render, get_object_or_404
from .models import ToDoList

# Create your views here.


def todo_list(request):
    todo_list = ToDoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": todo_list})


def todo_list_detail(request, id):
    todolist = get_object_or_404(ToDoList, id=id)
    return render(request, "todo_list_detail.html", {"todolist": todolist})
