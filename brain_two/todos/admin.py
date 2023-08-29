from django.contrib import admin
from .models import ToDoList

# Register your models here.


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(ToDoList, ToDoListAdmin)
