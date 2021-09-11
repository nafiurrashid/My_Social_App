from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import Widget

class CreateNewUser(UserCreationForm):
    email=forms.EmailField(required=True,label="", 
    widget=forms.TextInput(attrs={'placeholder':'Email'})),
    username=forms.EmailField(required=True,label="", 
    widget=forms.TextInput(attrs={'placeholder':'Username'})),

    
    class Meta:
        model=User
        fields= ('email','username', 'password1','password2')