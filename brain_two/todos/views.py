from django.shortcuts import render, get_object_or_404, redirect
from todos.forms import TodoListForm
from .models import ToDoList
from django.urls import reverse_lazy
from django.views.generic import DeleteView


# Create your views here.


def todo_list(request):
    todo_list = ToDoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": todo_list})


def todo_list_detail(request, id):
    todolist = get_object_or_404(ToDoList, id=id)
    return render(
        request, "todos/todo_list_detail.html", {"todolist": todolist}
    )


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail.html", id=todo_list.id)
    else:
        form = TodoListForm()
    return render(request, "todos/create_todo_list.html", {"form": form})


def todo_list_update(request, id):
    todo_list = get_object_or_404(ToDoList, id=id)

    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list)

    return render(
        request,
        "todos/todo_list_update.html",
        {"form": form, "todo_list": todo_list},
    )


class TodoListDeleteView(DeleteView):
    model = ToDoList
    template_name = "todos/todo_list_delete.html"
    success_url = reverse_lazy("todo_list_list")
