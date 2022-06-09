from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin as login
from . forms import Signup

    

def signup(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()  
        return redirect('/')  
    else:
        form = UserCreationForm()
    return render(response, 'account/signup.html', {'form': form})


def profile(response):
    return render(response, 'account/profile.html')

def settings(response):
    return render(response, 'account/settings.html')


