from django.urls import path
from . import views
from .views import TodoListDeleteView

urlpatterns = [
    path(
        "",
        views.todo_list,
        name="todo_list_list",
    ),
    path("<int:id>/", views.todo_list_detail, name="todo_list_detail"),
    path("create/", views.create_todo_list, name="todo_list_create"),
    path("<int:id>/edit/", views.todo_list_update, name="todo_list_update"),
    path(
        "<int:pk>/delete/",
        TodoListDeleteView.as_view(),
        name="todo_list_delete",
    ),
]
