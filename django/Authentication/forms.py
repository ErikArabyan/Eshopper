from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'required', 'type': 'username', 'placeholder': 'Enter your Username'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'required': 'required', 'placeholder': 'Enter your Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder': 'Password confirmation'}))
    def clean_username(self):
            return self.cleaned_data.get("username")
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'required': 'required', 'placeholder': 'Enter your Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder': 'Enter your password'}))
    class Meta:
        model = CustomUser
        fields = ['email', 'password']