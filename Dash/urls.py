"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DashApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('index/',views.HomePage,name='index'),
    path('logout/',views.LogoutPage,name='logout'),  
    path('lire-fichierso/', views.readfileso, name='readfileso'),
    path('lire-fichiertn1/', views.readfiletn1, name='readfiletn1'),
    path('lire-fichiertn2/', views.readfiletn2, name='readfiletn2'),
    path('lire-fichierint/', views.readfileint, name='readfileint'),
    
    path('update_table/', views.HomePage, name='update_table'),
    

]