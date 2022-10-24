from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=='POST':
        category = request.POST.get('category')
        form = ArticleForm(request.POST, request.FILES)  
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.category = category
            forms.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        category = request.POST.get('category')
        if form.is_valid():
            forms = form.save(commit=False)
            forms.category = category
            forms.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def python(request):
    articles = Article.objects.filter(category='Python').order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/python.html', context)

def django(request):
    articles = Article.objects.filter(category='Django').order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/django.html', context)

def javascript(request):
    articles = Article.objects.filter(category='JavaScript').order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/javascript.html', context)

def sql(request):
    articles = Article.objects.filter(category='SQL').order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/sql.html', context)

def css(request):
    articles = Article.objects.filter(category='CSS').order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/css.html', context)

def html(request):
    articles = Article.objects.filter(category='HTML').order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request,'articles/html.html', context)