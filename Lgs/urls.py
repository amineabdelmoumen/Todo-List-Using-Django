
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.register, name='register'), 
    path('/login', views.loginPage, name='loginPage'),  
    path('/home',views.homepage,name="home"),
    path('/logout',views.logoutPage, name="logout")
]