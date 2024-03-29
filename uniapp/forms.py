from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import MyModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['username','plan','wallet_address','amount']