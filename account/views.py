from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def login(response):
    form = UserCreationForm()
    return render(response, 'account/login.html', {'form': form})

def signup(response):
    form = UserCreationForm()
    return render(response, 'account/signup.html', {'form': form})

def logout(response):
    form = UserCreationForm()
    return render(response, 'account/logout.html', {'form': form})
