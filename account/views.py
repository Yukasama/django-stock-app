from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . forms import Signup, ChangeUsername
from django.core.mail import send_mail

    

def signupView(request):
    form = Signup()
    icons = ["user", "key", "key"]
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
    return render(request, 'account/signup.html', {'form': form, "icons": icons})



def loginView(request):

    #Check if User is logged in => Send him back
    if request.user.is_authenticated:
        return redirect('home')
    
    #Validate Login Data
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        
        #Check if User exists
        try: user = User.objects.get(username=username)
        except: messages.error(request, "User doesn't exist.")
        user = authenticate(request, username=username, password=password)
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
        form = ChangeUsername(request.POST)
        if "edit_username" in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            print(request.user.username, username)
            if not User.objects.filter(username=username).exists():   
                user = authenticate(username=request.user.username, password=password)
                print(user, request.user.username)
                if user is not None and form.is_valid():
                    x = form.save(commit=False)
                    x.username = username
                    x.save()
                else: 
                    messages.error(request, "Credentials do not match.")
            else:
                messages.error(request, "Username already exists.")
                

    page = "profile"
    data = {
        "page": page,
    }
    
    return render(request, 'account/profile.html', data)



@login_required(login_url='login')
def settings(request):
    return render(request, 'account/settings.html')


