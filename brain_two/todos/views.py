from django.shortcuts import render, get_object_or_404, redirect
from todos.forms import TodoListForm
from .models import ToDoList
# Create your views here.


def todo_list(request):
    todo_list = ToDoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": todo_list})


def todo_list_detail(request, id):
    todolist = get_object_or_404(ToDoList, id=id)
    return render(request, "todo_list_detail.html", {"todolist": todolist})


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail.html", id=todo_list.id)
    else:
        form = TodoListForm()
    return render(request, "todos/create_todo_list.html", {"form": form})
