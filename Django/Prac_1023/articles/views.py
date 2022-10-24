from django.shortcuts import render, redirect
from .forms import ArticleForm
# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)