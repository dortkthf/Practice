from django.shortcuts import render, redirect
from .forms import BoardForm
from .models import Board
# Create your views here.
def index(request):
    board = Board.objects.order_by('-pk')
    context = {
        'board' : board
    }
    return render(request, 'board/index.html', context)

def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('board:index')
    else:
        form = BoardForm()
    context = {
        'form' : form
    }
    return render(request,'board/create.html', context)

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board' : board
    }
    return render(request,'board/detail.html',context)

def update(request,pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('board:detail', pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'form' : form,
        'board' : board,
    }
    return render(request,'board/update.html',context)

def delete(request,pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('board:index')