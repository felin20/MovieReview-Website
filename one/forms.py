from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from django.contrib.auth import validators
from django.forms import ValidationError,ModelForm
from .models import *





class Regform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class revform(forms.ModelForm):
    class Meta:
        model = Userreview
        fields = ['Moviename', 'Review', 'Rating', 'pic']

