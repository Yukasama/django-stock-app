from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signupView, name='signup'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
]