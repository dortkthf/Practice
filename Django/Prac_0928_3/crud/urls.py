from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
    path("", views.read, name="read"),
    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]
