from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.order_by('-pk')
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.article = article
            cmt.save()
            return redirect('articles:detail', pk)
    else:
        form = CommentForm()
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
        'form' : form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'pk' : pk,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def c_delete(request, a_pk, c_pk):
    comment = Comment.objects.get(pk=c_pk)
    comment.delete()
    return redirect('articles:detail', a_pk)