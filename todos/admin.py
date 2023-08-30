from django.contrib import admin
from .models import TodoList, TodoItem

# Register your models here.


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(TodoList, TodoListAdmin)


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("task", "due_date", "is_completed")


admin.site.register(TodoItem, TodoItemAdmin)
