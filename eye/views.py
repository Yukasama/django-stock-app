from django.shortcuts import render
from eye.models import Stock


def stocks(request):
    return render(request, 'eye/stocks.html')

def calendar(request):
    return render(request, 'eye/calendar.html')

def education(request):
    return render(request, 'eye/education.html')

def screener(request):
    return render(request, 'eye/screener.html')

def portfolio(request):
    return render(request, 'eye/portfolio.html')


def symbol(request, symbol):
    symbol = Stock.objects.get(symbol=symbol)
    return render(request, 'eye/symbol.html', {'symbol': symbol})