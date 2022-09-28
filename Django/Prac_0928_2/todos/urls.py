from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.read, name="read"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
]
