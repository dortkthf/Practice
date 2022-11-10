
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    # 페이지네이션
    page = request.GET.get('page')
    paginator = Paginator(articles, 6)
    page_obj = paginator.get_page(page)
    context = {
        'articles' : articles,
        'page_list' : page_obj,
        'paginator' : paginator,
    }
    return render(request, 'articles/index.html', context)

@login_required
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
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.article = article
            forms.save()
            return redirect('articles:detail', pk)
    else:
        form = CommentForm()
    comments = article.comments.order_by('-pk')
    context = {
        'article' : article,
        'form' : form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
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

@login_required
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

def search(request):
    search = request.GET.get('search')
    ctg = request.GET.get('category')

    if ctg == 'Python':
        articles = Article.objects.filter(
            category=ctg,
            content__contains=search
            ) | Article.objects.filter(
            category=ctg,
            title__contains=search
            )
    elif ctg == 'Django':
        articles = Article.objects.filter(
            category=ctg,
            content__contains=search
            ) | Article.objects.filter(
            category=ctg,
            title__contains=search
            )    
    elif ctg == 'JavaScript':
        articles = Article.objects.filter(
            category=ctg,
            content__contains=search
            ) | Article.objects.filter(
            category=ctg,
            title__contains=search
            )
    elif ctg == 'SQL':
        articles = Article.objects.filter(
            category=ctg,
            content__contains=search
            ) | Article.objects.filter(
            category=ctg,
            title__contains=search
            )
    elif ctg == 'CSS':
        articles = Article.objects.filter(
            category=ctg,
            content__contains=search
            ) | Article.objects.filter(
            category=ctg,
            title__contains=search
            )
    elif ctg == 'HTML':
        articles = Article.objects.filter(
            category=ctg,
            content__contains=search
            ) | Article.objects.filter(
            category=ctg,
            title__contains=search
            )
    page = request.GET.get('page')
    paginator = Paginator(articles, 6)
    page_obj = paginator.get_page(page)            
    context = {
        'articles' : articles,
        'ctg' : ctg,
        'search' : search,
        'page_list' : page_obj,
        'paginator' : paginator,
    }
    return render(request, 'articles/search.html', context)

def mainsearch(request):
    search = request.GET.get('mainsearch')
    articles = Article.objects.filter(title__contains=search) | Article.objects.filter(content__contains=search)
    page = request.GET.get('page')
    paginator = Paginator(articles, 6)
    page_obj = paginator.get_page(page)  
    context = {
        'articles' : articles,
        'search' : search,
        'page_list' : page_obj,
        'paginator' : paginator,
    }
    return render(request, 'articles/mainsearch.html', context)

@login_required
def c_delete(request, a_pk, c_pk):
    comment = Comment.objects.get(pk=c_pk)
    comment.delete()
    return redirect('articles:detail', a_pk)

@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    if article in request.user.like_articles.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', pk)