from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.task_list, name="task_list"),
    path(
        "tasks/<int:task_id>/complete/",
        views.complete_task,
        name="complete_task",
    ),
    path(
        "tasks/<int:task_id>/delete/",
        views.delete_task,
        name="delete_task",
    ),
]
