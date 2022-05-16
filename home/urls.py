from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    
    path('aboutus', views.aboutus, name='aboutus'),
    path('careers', views.careers, name='careers'),
    path('faq', views.faq, name='faq'),
    path('pricing', views.pricing, name='pricing'),
    path('development', views.development, name='development'),
    path('newsletter', views.newsletter, name='newsletter'),
    
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    
    
    path('contact', views.contact, name='contact')
]