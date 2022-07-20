from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signupView, name='signup'),
    path('login', views.loginView, name='signin'),
    path('logout', views.logoutView, name='logout'),
    
    path('', views.account, name='account'),
    
    path('password-reset', views.passwordReset, name="password-reset"),
    path('two-factor', views.twoFactor, name="two-factor"),
    path('authorize', views.authorize, name="authorize"),
    path('verify', views.verify, name="verify"),

]