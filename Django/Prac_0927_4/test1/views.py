from django.shortcuts import render

# Create your views here.
def index(request, name):
    return render(request, "test1/index.html", {"name": name})
