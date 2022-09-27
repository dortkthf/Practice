from django.shortcuts import render
import random

# Create your views here.
def oddEven(request, number):
    context = {
        "number": number,
    }
    return render(request, "fstapp/oddEven.html", context)


def calculator(request, number1, number2):
    context = {
        "number1": number1,
        "number2": number2,
    }
    return render(request, "fstapp/calculator.html", context)


def pastLife(request):

    return render(request, "fstapp/pastLife.html")


def pastLife_result(request):
    name = request.GET.get("name")
    pastL = ["사자", "호랑이", "늑대"]
    past = random.choice(pastL)
    if past == "호랑이":
        img = "https://sojoong.joins.com/wp-content/uploads/sites/4/2021/07/KakaoTalk_20210708_191738164.jpg"
    elif past == "사자":
        img = "https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202001/01/c9fc6597-f43b-40f8-a1ae-ea3f0a426210.jpg"
    else:
        img = "https://img4.yna.co.kr/etc/inner/KR/2020/02/09/AKR20200209003700091_01_i_P4.jpg"
    context = {"name": name, "img": img, "past": past}
    return render(request, "fstapp/pastLife_result.html", context)


def kinput(request):

    return render(request, "fstapp/kinput.html")


def kresult(request):
    pnum = request.GET.get("pnum")
    pn = list(range(int(pnum)))
    pword = request.GET.get("pword")
    pw = list(range(int(pword)))
    context = {"pnum": pnum, "pword": pword, "pn": pn, "pw": pw}
    return render(request, "fstapp/kresult.html", context)
