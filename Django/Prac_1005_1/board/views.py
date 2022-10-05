from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
# Create your views here.

def index(request):
    board = Board.objects.order_by('-pk')
    context = {
        'board' : board,
    }
    return render(request,'board/index.html', context)

def create(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()
            return redirect('board:index')
    else:
        board_form = BoardForm()
    context = {
        'board_form' : board_form,
    }
    return render(request, 'board/create.html', context)

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board' : board,
    }
    return render(request, 'board/detail.html',context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board_form = BoardForm(request.POST, instance=board)
        if board_form.is_valid():
            board_form.save()
            return redirect ('board:detail', board.pk)
    else:
        board_form = BoardForm(instance=board)
    context = {
        'board_form' : board_form,
        'board' : board
    }
    return render(request, 'board/update.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('board:index')