from django.forms import ModelForm
from todos.models import ToDoList


class TodoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ("name",)


# class TodoItemForm(ModelForm):
#     class Meta:
#         model = TodoItem
#         fields = (
#             "task",
#             "due_date",
#             "is_completed",
#             "list",
#         )
