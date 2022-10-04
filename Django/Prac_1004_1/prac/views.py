from django.shortcuts import render, redirect
from . models import Crud
from .forms import CrudForm
# Create your views here.
def index(request):
    crud = Crud.objects.order_by('-pk')
    context = {
        'crud' : crud
    }
    return render(request, 'prac/index.html', context)

def create(request):
    if request.method == 'POST':
        crud_form = CrudForm(request.POST)
        if crud_form.is_valid():
            crud_form.save()
            return redirect('prac:index')
    else:
        crud_form = CrudForm()
    context = {
        'crud_form' : crud_form
    }
    return render(request, 'prac/new.html', context)

def detail(request, pk):
    crud = Crud.objects.get(pk=pk)
    context = {
        'crud' : crud
    }
    return render (request, 'prac/detail.html', context)

def update(request, pk):
    crud = Crud.objects.get(pk=pk)
    if request.method == 'POST':
        crud_form = CrudForm(request.POST, instance=crud)
        if crud_form.is_valid():
            crud_form.save()
            return redirect('prac:detail', crud.pk)
    else:
        crud_form = CrudForm(instance=crud)
    context = {
        'crud_form' : crud_form,
        'pk' : pk
    }
    return render(request, 'prac/update.html', context)

def delete(request, pk):
    crud = Crud.objects.get(pk=pk)
    crud.delete()
    return redirect('prac:index')