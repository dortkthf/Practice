from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create-end/", views.create_end, name="create_end"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("update/<int:pk>", views.update, name="update"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
