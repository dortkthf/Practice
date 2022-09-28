from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    data = Todo.objects.all()
    context = {
        "data": data,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    Todo.objects.create(content=content)

    return redirect("todos:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todos:index")
