from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . forms import Signup
from django.core.mail import send_mail
from account.forms import Profile

    

def signupView(request):
    form = Signup()
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            send_mail(
                "Aethega | Sign Up Notification",
                "You just created an account on Aethega!",
                "yukasamaa@gmail.com",
                ["daszehntefragezeichen@gmail.com"],
                fail_silently=False,
            )
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error during registration.")
    return render(request, 'account/signup.html', {'form': form})



def loginView(request):

    #Check if User is logged in => Send him back
    if request.user.is_authenticated:
        return redirect('home')
    
    #Validate Login Data
    if request.method == "POST":
        userauth = request.POST.get("userauth").lower()
        password = request.POST.get("password")
        
        #Check for Email or Username Login
        emailLogin = True
        if User.objects.get(username=userauth).exists(): emailLogin = False
        elif User.objects.get(email=userauth).exists(): pass
        else: messages.error(request, "User doesn't exist.")
        
        user = authenticate(email=userauth, password=password) if emailLogin == True else authenticate(username=userauth, password=password)
        if user is not None:
            login(request, user) #Logging in User
            return redirect("home")
        else:
            messages.error(request, "Credentials doesn't match.")
            
    return render(request, 'registration/login.html')



@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('home')



@login_required(login_url='login')
def profile(request):
    if (request.method == "POST"):
        if "edit_username" in request.POST:
            newUsername = request.POST["username"]
            password = request.POST["password"]
            if not User.objects.filter(username=newUsername).exists():   
                user = authenticate(username=request.user.username, password=password)
                if user is not None:
                    user.username = newUsername
                    user.save()
                    return redirect("profile")
                else: 
                    messages.error(request, "Credentials do not match.")
            else:
                messages.error(request, "Username already exists.")
        elif "edit_email" in request.POST:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                user.email = email
                user.save()
                return redirect("profile")
            else: 
                messages.error(request, "Credentials do not match.")
        elif "edit_biography" in request.POST:
            user = User.objects.get(pk=request.user.id)
            biography = request.POST["biography"]
            user.profile.biography = biography
            user.save()
                

    page = "profile"
    data = {
        "page": page,
    }
    
    return render(request, 'account/profile.html', data)



@login_required(login_url='login')
def settings(request):
    return render(request, 'account/settings.html')


