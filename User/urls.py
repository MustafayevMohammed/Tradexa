from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "User"

urlpatterns = [
    path("",views.CreatePost,name="create_post"),
    path("register/",views.register,name="register"),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logout,name="logout"),
]
