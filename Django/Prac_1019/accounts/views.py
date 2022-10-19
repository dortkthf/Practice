from django.shortcuts import render, redirect
from .forms import SignupForm, UpdateForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = SignupForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/userlogin.html', context)

def userlogout(request):
    logout(request)
    return redirect('articles:index')

def userupdate(request):
    if request.method=='POST':
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail')
    else:
        form = UpdateForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/userupdate.html', context)

def change_password(request):
    if request.method == 'POST':
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
    return render(request, 'accounts/change_password.html', context)

def delete(request):
    request.user.delete()
    logout(request)
    return redirect('accounts:index')

def detail(request):
    return render(request, 'accounts/detail.html')