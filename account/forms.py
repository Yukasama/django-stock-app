from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    email = forms.CharField(max_length=500)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(Signup, self).__init__(*args, **kwargs)

