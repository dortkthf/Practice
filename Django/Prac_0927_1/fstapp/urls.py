from django.urls import path
from . import views

urlpatterns = [
    path("oddEven/<int:number>", views.oddEven),
    path("calculator/<int:number1>/<int:number2>", views.calculator),
    path("past-life/", views.pastLife),
    path("past-life-result/", views.pastLife_result),
    path("klorem-input/", views.kinput),
    path("klorem-result/", views.kresult),
]
