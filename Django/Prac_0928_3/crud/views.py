from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def read(request):
    todos = Todo.objects.all()

    context = {
        "todos": todos,
    }
    return render(request, "crud/read.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect("crud:read")


def delete(request):
    pklist = request.POST.getlist("pk")
    for pk in pklist:
        Todo.objects.get(id=pk).delete()
    return redirect("crud:read")


def update(request):
    pklist = request.POST.getlist("pk")
    for pk in pklist:
        udt = Todo.objects.get(id=pk)
        if udt.completed == True:
            udt.completed = False
            udt.save()
        else:
            udt.completed = True
            udt.save()
    return redirect("crud:read")
