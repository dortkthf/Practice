from django.shortcuts import render

from .models import Article

# guestbook = []
# Create your views here.
# DB에서 가져오기
def index(request):
    guestbook = Article.objects.all()
    # SELECT * FROM aricles;
    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    # guestbook.append(content)
    # DB에 저장
    Article.objects.create(content=content)
    return render(request, "articles/create.html", {"content": content})
