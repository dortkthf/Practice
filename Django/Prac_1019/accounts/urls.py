from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('update/', views.userupdate, name='userupdate'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('detail/', views.detail, name='detail')
]