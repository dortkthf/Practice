from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('python/', views.python, name='python'),
    path('django/', views.django, name='django'),
    path('javascript/', views.javascript, name='javascript'),
    path('sql/', views.sql, name='sql'),
    path('css/', views.css, name='css'),
    path('html/', views.html, name='html'),
    path('search/', views.search, name='search'),
    path('mainsearch/', views.mainsearch, name='mainsearch'),
    path('<int:a_pk>/comment/<int:c_pk>', views.c_delete, name='c_delete'),
    path('like/<int:pk>', views.like, name='like'),
]