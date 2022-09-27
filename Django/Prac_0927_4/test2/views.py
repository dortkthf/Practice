from django.shortcuts import render
from .models import Test2

# Create your views here.
def index(request):
    userlist = Test2.objects.all()
    return render(request, "test2/index.html", {"userlist": userlist})


def index_result(request):
    eid = request.GET.get("id")
    pw = request.GET.get("pw")
    Test2.objects.create(eid=eid, pw=pw)
    context = {
        "eid": eid,
        "pw": pw,
    }
    return render(request, "test2/index_result.html", context)
