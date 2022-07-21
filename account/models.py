from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from Aethega import settings
import os

class AccountManager(BaseUserManager):
    
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError("E-Mail required for User Creation")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    



def get_profile_image_filepath(self, filename):
    if not os.path.exists(f"static/account/img/profile_images/{self.pk}"):
        os.makedirs(f"static/account/img/profile_images/{self.pk}")
    return f'static/account/img/profile_images/{self.pk}/profile_image.png'

def get_profile_image_default():
    return "static/account/img/profile_images/DefaultUser.png"



class Account(AbstractBaseUser):
    
    #Individual User Fields
    username = models.CharField(max_length=50, default="Guest")
    email = models.EmailField(max_length=100, unique=True)
    
    #Custom User Fields
    biography = models.TextField(default="My interesting Biography...")
    profile_image = models.ImageField(upload_to=get_profile_image_filepath, blank=True, null=True, default=get_profile_image_default)
    
    #User Verification
    email_verified = models.BooleanField(default=False)
    AUTH_CHOICES = (
        ("Email", "Email"),
        ("SMS", "SMS"),
        ("Google Auth", "Google Authenticator"),
    )
    two_factor_auth = models.CharField(choices=AUTH_CHOICES, max_length=20, null=True, blank=True, default=None)
    two_factor_key = models.CharField(blank=True, null=True, max_length=10)
    
    #Custom User Permissions
    hide_email = models.BooleanField(default=True)
    profile_private = models.BooleanField(default=False)
    show_investments = models.BooleanField(default=False)
    
    #Logging Dates
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    
    #Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    #BaseUserManager
    objects = AccountManager()

    #Switch Email to Authentication instead of Username
    USERNAME_FIELD = "email"
    
    #User Functions
    def __str__(self):
        return self.username
    
    def profile_img_file(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    

