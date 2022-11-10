from django.shortcuts import render, redirect
from accounts.forms import SignupForm, UpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = SignupForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = UpdateForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/password.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def follow(request, pk):
    user = User.objects.get(pk=request.user.pk)
    other = User.objects.get(pk=pk)
    if user in other.followers.all():
        user.followings.remove(other)
    else:
        user.followings.add(other) 
    return redirect('accounts:detail', pk)