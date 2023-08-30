from django.shortcuts import render, get_object_or_404, redirect
from todos.forms import TodoListForm, TodoItemForm
from todos.models import TodoList, TodoItem


# Create your views here.


def todo_list(request):
    todo_list = TodoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": todo_list})


def todo_list_detail(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    return render(
        request, "todos/todo_list_detail.html", {"todolist": todolist}
    )


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoListForm()
    return render(request, "todos/create_todo_list.html", {"form": form})


def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)

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


def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)

    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")
    return render(
        request, "todos/todo_list_delete.html", {"todo_list": todo_list}
    )


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save()
            return redirect("todo_list_detail", id=todo_item.list.id)
    else:
        form = TodoItemForm()
    return render(request, "todos/todo_item_create_form.html", {"form": form})


def todo_item_update(request, id):
    todo_item = get_object_or_404(TodoItem, id=id)

    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=todo_item.list.id)
    else:
        form = TodoItemForm(instance=todo_item)

    return render(
        request,
        "todos/todo_item_update.html",
        {"form": form, "todo_item": todo_item},
    )
