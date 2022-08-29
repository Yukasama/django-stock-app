from django.urls import path
from . import views


urlpatterns = [
    path('stocks', views.stocks, name='stocks'),
    
    path('calendar', views.calendar, name='calendar'),
    path('news', views.news, name='news'),
    path('education', views.education, name='education'),
    path('education/neuralnetwork', views.neuralNetwork, name='education'),
    path('screener', views.screener, name='screener'),
    path('portfolio', views.portfolio, name='portfolio'),
    
    path('stocks/<str:symbol>', views.symbol, name='symbol'),
    path('algorithm', views.algorithm, name="algorithm"),
]