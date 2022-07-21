from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.backends import EmailBackend as auth
from account.models import AccountManager
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from account.models import Account

    
    
def signupView(request):
    
    #Check if User is logged in => Send him back
    if request.user.is_authenticated:
        return redirect('home')
     
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
def account(request):
    if (request.method == "POST"):
        if "edit_username" in request.POST:
            new_username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(email=request.user.email, password=password)
            if user is not None:
                user.username = new_username
                user.save()
                return redirect("account")
            else: 
                messages.error(request, "Credentials do not match.")
        elif "edit_email" in request.POST:
            new_email = request.POST["email"].lower()
            password = request.POST["password"]
            user = auth.authenticate(email=request.user.email, password=password)
            if user is not None:
                user.email = new_email
                user.save()
                return redirect("account")
            else: 
                messages.error(request, "Credentials do not match.")
        elif "edit_biography" in request.POST:
            user = Account.objects.get(pk=request.user.id)
            biography = request.POST["biography"]
            user.biography = biography
            user.save()
            return redirect("account")
        elif "edit_profile_image" in request.POST:
            user = Account.objects.get(pk=request.user.id)
            new_profile_image = request.FILES["profile_image"]
            user.profile_image = new_profile_image
            user.save()
            return redirect("account")
    elif "change_password" in request.GET:
        return redirect("authorize")
            
                

    page = "account"
    data = {
        "page": page,
    }
    
    return render(request, 'account/account.html', data)



@login_required(login_url='signin')
def passwordReset(request):
    if request.method == "POST":
        #Check if User has 2 Factor Authentification enabled
        email = request.user.email
        user = Account.objects.get(email=email)
        password = request.POST["oldpassword"]
        new_password = request.POST["newpassword"]
        repeat_password = request.POST["repeatpassword"]
        
        if auth.authenticate(email=email, password=password) is not None:
            password_validation = auth.password_validator(email, new_password)
            if password_validation != new_password:
                messages.error(request, password_validation)
            else:    
                user.set_password(new_password)
                user.save()
                redirect("account")
    else:
        return redirect("authorize")                
    
    return render(request, 'account/password_reset.html')



def authorize(request):    
    referer = request.META.get('HTTP_REFERER')
    print(referer)
    if request.method == "POST":
        email = request.POST["email"]
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email=email)
            user.two_factor_key = "083959"
            #sendmail
            return render(request, 'account/verify.html', {"email": email})
        else:
            messages.error(request, "Account with this E-Mail does not exist.")        
            
    return render(request, 'account/authorize.html')



def verify(request):
    referer = request.META['HTTP_REFERER']
    print(referer)
    if referer == "http://127.0.0.1:8000/account/authorize" or referer == "http://127.0.0.1:8000/account/verify":
        if request.method == "POST":
            verification = request.POST["verification"]
            user = Account.objects.get(email=email)
            print(user.two_factor_key)
            if verification == user.two_factor_key:
                return redirect("password-reset")
            else:
                messages.error(request, "Verification Code does not match.")
    else:
        return redirect("home")
            
    
    return render(request, 'account/verify.html')



@login_required(login_url='signin')
def twoFactor(request):
    return render(request, 'account/two_factor.html')


