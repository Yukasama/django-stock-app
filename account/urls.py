from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signupView, name='signup'),
    path('login', views.loginView, name='signin'),
    path('logout', views.logoutView, name='logout'),
    
    path('profile', views.profile, name='profile'),
    
    path('password-change', views.passwordChange, name="password-change"),
    path('password-reset', views.passwordReset, name="password_reset"),
    path('factor2-auth', views.factor2Auth, name="factor2_auth"),
]