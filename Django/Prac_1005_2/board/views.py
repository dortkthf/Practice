from django.shortcuts import render, redirect
from .forms import BoardForm
from .models import Board
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
    return render(request,'board/create.html', context)