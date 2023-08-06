from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('signup/', views.user_signup, name ='signup'),
    path('login/', views.user_login, name ='login'),
    path('dashboard/', views.profile, name ='profile'),
    path('logout/', views.user_logout, name ='logout'),
    path('changepassword/', views.changepassword, name ='changepassword'),
]