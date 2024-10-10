from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']