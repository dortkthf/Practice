from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def read(request):
    todos = Todo.objects.all()

    context = {
        "todos": todos,
    }
    return render(request, "todos/read.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect("todos:read")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todos:read")


def update(request, pk):
    udt = Todo.objects.get(id=pk)
    if udt.completed == True:
        udt.completed = False
        udt.save()
    else:
        udt.completed = True
        udt.save()

    return redirect("todos:read")
