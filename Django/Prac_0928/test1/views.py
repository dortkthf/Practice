from django.shortcuts import render
from .models import Test1

# Create your views here.
def index(request):
    userlist = Test1.objects.all()
    context = {"userlist": userlist}
    return render(request, "test1/index.html", context)


def index_result(request):
    email = request.GET.get("email")
    nickname = request.GET.get("nickname")
    pw = request.GET.get("pw")
    Test1.objects.create(nickname=nickname, email=email, pw=pw)
    context = {
        "email": email,
        "nickname": nickname,
        "pw": pw,
    }
    return render(request, "test1/index_result.html", context)
