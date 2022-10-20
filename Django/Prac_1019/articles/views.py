
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    article = Article.objects.order_by('-pk')
    context = {
        'article' : article,
    }
    return render(request,'articles/index.html', context)

@login_required
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

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, '수정 완료')
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
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    else:
        messages.warning(request, '회원정보가 일치하지 않습니다.')
        return redirect('articles:detail', article.pk)

@login_required
def c_delete(request, a_pk, c_pk):
    comment = Comment.objects.get(pk=c_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', a_pk)

def c_update(request, a_pk, c_pk):
    article = Article.objects.get(pk=a_pk)
    comments = Comment.objects.get(pk=c_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comments)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', a_pk)
    else:
        form = CommentForm(instance=comments)
    context = {
        'form' : form,
        'article' : article,
        'comments' : comments
    }
    return render(request, 'articles/c_update.html', context)