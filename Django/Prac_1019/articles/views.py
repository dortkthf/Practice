from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article
# Create your views here.

def index(request):
    article = Article.objects.order_by('-pk')
    context = {
        'article' : article,
    }
    return render(request,'articles/index.html', context)

def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            create = form.save(commit=False)
            create.user = request.user
            create.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
    else:
        comment_form = CommentForm()
    comments = article.comment_set.order_by('-pk')
    context = {
        'article' : article,
        'form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
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