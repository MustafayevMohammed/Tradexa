from django.db import models
from django.db.models import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from . import models
from . import forms
from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError
from django.contrib.auth import logout as django_logout


# Create your views here.

# class CreatePost(CreateView):
#     model = models.PostModel
#     fields = ['text']
#     template_name = "add.html"
#     success_url = ""

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return redirect("User:create_post")


def CreatePost(request):
    form = forms.PostForm()
    posts = models.PostModel.objects.all().using('users_posts_db')

    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("User:create_post")

    context = {
        "form":form,
        "posts":posts
    }
    return render(request,"add.html",context)

# class RegisterView(CreateView):
#     model = User
#     fields = ["first_name","last_name","email","username","password"]
#     template_name = "register.html"
#     success_url = "User:login"

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.save()
#         return redirect("User:login")


def logout(request):
    django_logout(request)
    return redirect("User:create_post")


def register(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("User:login")

    context = {
    "form":form
    }
    return render(request,"register.html",context)

def loginPage(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        account = authenticate(request,username=username,password=password)
        if account is None:
            raise ValidationError(request,"Username or Password is false")
        else:
            login(request,account)
            return redirect("User:create_post")

    context = {
        "form":form
    }
    return render(request,"login.html",context)