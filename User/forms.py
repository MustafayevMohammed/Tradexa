from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields, widgets
from django.forms.forms import Form
from django.contrib.auth.models import User
from . import models


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'fields'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'fields'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'fields'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'fields'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'passfields'})
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class':'passfields'})
    )
    
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]


class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'fields'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'fields'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ["text",]