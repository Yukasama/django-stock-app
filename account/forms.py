from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Profile


class Signup(UserCreationForm):
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    username = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(Signup, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs={'placeholder': 'Username', 'class': 'input input_valid'}
        self.fields['password1'].widget.attrs={'placeholder': 'Password', 'class': 'input input_valid'}
        self.fields['password2'].widget.attrs={'placeholder': 'Repeat Password', 'class': 'input input_valid'}

        



