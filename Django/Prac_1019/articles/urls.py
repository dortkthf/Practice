from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:a_pk>/c_delete/<int:c_pk>/', views.c_delete, name='c_delete'),
    path('<int:a_pk>/c_update/<int:c_pk>/', views.c_update, name='c_update'),
]