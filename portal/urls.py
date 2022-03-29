from django import views
from  django.urls import path
from .import views

# Create your views here.
urlpatterns = [
    path('',views.home,name='index'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('dash',views.dashboard,name='dashboard'),
    path('update',views.updateprofile,name='update')
    ]
