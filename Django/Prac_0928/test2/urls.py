from django.urls import path
from . import views

app_name = "test2"

urlpatterns = [
    path("index2/", views.index2),
    path("index2-result/", views.index2_result),
]
