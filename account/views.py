from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.backends import EmailBackend as auth
from account.models import AccountManager
from django.contrib.auth import login
from django.core.mail import send_mail
from account.models import Account

    

def signupView(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password1"]
        confpassword = request.POST["password2"]
        
        #Does E-Mail exist
        if Account.objects.filter(email=email).exists():
            messages.error(request, "E-Mail is already registered.")
        else:   
            #Password Error Handling
            password_validation = auth.password_validator(email, password)
            if password_validation != password:
                messages.error(request, password_validation)
            else:    
                #Do both Passwords match
                if password == confpassword:
                    if not Account.objects.filter(email=email).exists():
                        user = Account.objects.create_user(email=email, password=password)
                        user.save()
                        # send_mail(
                        #     "Aethega | Sign Up Notification",
                        #     "You just created an account on Aethega!",
                        #     "yukasamaa@gmail.com",
                        #     ["daszehntefragezeichen@gmail.com"],
                        #     fail_silently=False,
                        # )
                        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        messages.success(request, "You successfully signed up.")
                        return redirect('home')
                else:
                    messages.error(request, "Passwords don't match.")
    return render(request, 'account/signup.html')



def loginView(request):

    #Check if User is logged in => Send him back
    if request.user.is_authenticated:
        return redirect('home')
    
    #Validate Login Data
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
           
        #Check if User exists
        user = auth.authenticate(email=email, password=password)
            
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("home")
        else:
            messages.error(request, "Credentials do not match.")
            
    return render(request, 'account/login.html')



@login_required(login_url='signin')
def logoutView(request):
    logout(request)
    return redirect('home')



@login_required(login_url='signin')
def profile(request):
    if (request.method == "POST"):
        if "edit_username" in request.POST:
            new_username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(email=request.user.email, password=password)
            if user is not None:
                user.username = new_username
                user.save()
                return redirect("profile")
            else: 
                messages.error(request, "Credentials do not match.")
        elif "edit_email" in request.POST:
            new_email = request.POST["email"].lower()
            password = request.POST["password"]
            user = auth.authenticate(email=request.user.email, password=password)
            if user is not None:
                user.email = new_email
                user.save()
                return redirect("profile")
            else: 
                messages.error(request, "Credentials do not match.")
        elif "edit_biography" in request.POST:
            user = Account.objects.get(pk=request.user.id)
            biography = request.POST["biography"]
            user.biography = biography
            user.save()
            return redirect("profile")
        elif "edit_profile_image" in request.POST:
            user = Account.objects.get(pk=request.user.id)
            new_profile_image = request.POST["profile_image"]
            user.profile_image = new_profile_image
            user.save()
            
                

    page = "profile"
    data = {
        "page": page,
    }
    
    return render(request, 'account/profile.html', data)



@login_required(login_url='signin')
def settings(request):
    return render(request, 'account/settings.html')


