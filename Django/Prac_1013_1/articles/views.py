from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    user = get_user_model().objects.all()
    context = {
        'user' : user
    }
    return render(request, 'articles/index.html', context)
    
@login_required
def create(request):
    return render(request,'articles/create.html')

