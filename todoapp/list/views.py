from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import ListForm, TaskForm
from .models import List, Task


@login_required(login_url="/login")
def create_list(request):
    """
    Endpoint which created a list for the logged in user
    and redirects to the list detail view if the list creation was successful
    """
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            new_list = form.save(user=request.user)
            new_list.save()
            return redirect("detail_list", new_list.pk)
    form = ListForm()
    return render(request=request, template_name="list/create_list.html", context={"form": form})


@login_required(login_url="/login")
def detail_list(request, list_id):
    """
    Endpoint to display details about the list
    """
    task_list = List.objects.get(id=int(list_id))
    tasks = Task.objects.filter(list=list_id)
    task_form = TaskForm()
    return render(
        request=request,
        template_name="list/detail_list.html",
        context={
            "list": task_list,
            "tasks": tasks,
            "task_form": task_form
        }
    )


@login_required(login_url="/login")
def create_task(request):
    """
    Endpoint to add new task to the list
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            new_task.save()
            return JsonResponse({"task": new_task.description})
        else:
            return JsonResponse({"error": form.errors})
    return JsonResponse({"error": "Invalid Request"})


@login_required(login_url="/login")
def mark_task(request, task_id):
    """
    Endpoint to mark or unmark a task is complete
    """
    if request.method == "POST":
        task = Task.objects.get(id=int(task_id))
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponse("Task Marked")


@login_required(login_url="/login")
def delete_task(request, task_id):
    """
    Endpoint to delete task from the list
    """
    if request.method == "POST":
        Task.objects.get(id=int(task_id)).delete()
        return HttpResponse("Task Deleted")
    return HttpResponse("Invalid Request")


@login_required(login_url="/login")
def delete_list(request, list_id):
    """
    Endpoint to delete list from the list
    """
    if request.method == "POST":
        task_list = List.objects.get(id=int(list_id))
        tasks = Task.objects.filter(list=task_list)
        tasks.delete()
        task_list.delete()
        return HttpResponse("List Deleted")
    return HttpResponse("Invalid Request")
