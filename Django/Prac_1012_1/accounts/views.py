from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:index')
        pass
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/index.html', context)