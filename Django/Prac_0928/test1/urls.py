from django.urls import path
from . import views

app_name = "test1"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("index-result/", views.index_result, name="result"),
]
