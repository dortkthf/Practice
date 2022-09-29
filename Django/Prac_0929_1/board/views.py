from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()

    context = {
        "boards": boards,
    }
    return render(request, "board/index.html", context)


def create(request):
    return render(request, "board/create.html")


def create_end(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    board = request.GET.get("board")

    Board.objects.create(title=title, content=content, board=board)

    return redirect("board:index")


def detail(request, pk):
    content = Board.objects.get(id=pk)
    context = {
        "content": content,
    }
    return render(request, "board/detail.html", context)


def update(request, pk):
    title = request.GET.get("title")
    content = request.GET.get("content")
    board = request.GET.get("board")
    board1 = Board.objects.get(id=pk)
    board1.title = title
    board1.content = content
    board1.board = board
    board1.save()

    return redirect("board:index")


def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()

    return redirect("board:index")
