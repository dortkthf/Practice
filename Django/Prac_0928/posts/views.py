from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    boarder = Post.objects.all()

    context = {
        "boarder": boarder,
    }
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):

    ## Parameter 로 날라온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # DB에 저장
    Post.objects.create(title=title, content=content)
    context = {
        "title": title,
        "content": content,
    }
    return redirect("posts:index")


def delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")
