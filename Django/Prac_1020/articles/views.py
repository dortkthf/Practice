from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comments
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    article = Article.objects.order_by('-pk')
    context = {
        'article' : article,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            userform = form.save(commit=False)
            userform.user = request.user
            userform.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment = article.comments_set.order_by('-pk')
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.article = article
            forms.save()
            return redirect('articles:detail', pk)
    else:
        form = CommentForm()
    context = {
        'article' : article,
        'form' : form,
        'comment' : comment,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES, instance = article)
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

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@login_required
def c_delete(request, a_pk, c_pk):
    comment = Comments.objects.get(pk=c_pk)
    comment.delete()
    return redirect('articles:detail', a_pk)