from django.contrib import admin
from .models import ToDoList , TodoItem

# Register your models here.


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(ToDoList, ToDoListAdmin)


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("task", "due_date", "is_completed")


admin.site.register(TodoItem, TodoItemAdmin)
