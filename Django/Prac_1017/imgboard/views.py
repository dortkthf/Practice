from django.shortcuts import render, redirect
from .forms import ImgForm
from .models import Imgboard
# Create your views here.
def index(request):
    imgs = Imgboard.objects.order_by('-pk')
    context = {
        'imgs' : imgs
    }
    return render(request,'imgboard/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imgboard:index')
    else:
        form = ImgForm()
    context = {
        'form' : form,
    }
    return render(request, 'imgboard/create.html', context)

def detail(request, pk):
    img = Imgboard.objects.get(pk=pk)
    context = {
        'img' : img,
    }
    return render(request, 'imgboard/detail.html', context)

def update(request, pk):
    img = Imgboard.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImgForm(request.POST,request.FILES, instance=img)
        if form.is_valid():
            form.save()
            return redirect('imgboard:detail', img.pk)
    else:
        form = ImgForm(instance=img)
    context = {
        'form' : form,
        'pk' : pk,
    }
    return render(request, 'imgboard/update.html', context)

def delete(request, pk):
    img = Imgboard.objects.get(pk=pk)
    img.delete()
    return redirect('imgboard:index')