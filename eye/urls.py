from django.urls import path
from . import views


urlpatterns = [
    path('stocks', views.stocks, name='stocks'),
    
    path('calendar', views.calendar, name='calendar'),
    path('screener', views.screener, name='screener'),
    path('portfolio', views.portfolio, name='portfolio'),
    
    path('stocks/', views.ticker, name='ticker'),
]