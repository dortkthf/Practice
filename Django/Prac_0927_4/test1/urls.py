from django.urls import path
from . import views

urlpatterns = [
    path("index/<str:name>", views.index),
]
