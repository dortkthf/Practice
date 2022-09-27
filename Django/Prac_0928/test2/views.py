from django.shortcuts import render

# Create your views here.
def index2(request):
    return render(request, "test2/index2.html")


def index2_result(request):
    return render(request, "test2/index2_result.html")
