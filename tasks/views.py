
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()

        if title:
            Task.objects.create(title=title)

        return redirect("task_list")

    return render(request, "tasks/home.html")


def task_list(request):
    tasks = Task.objects.order_by("completed", "-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def complete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()

    return redirect("task_list")


def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()

    return redirect("task_list")
