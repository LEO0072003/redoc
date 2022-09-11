from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username']