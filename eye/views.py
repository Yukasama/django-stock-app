from django.shortcuts import render


def stocks(request):
    return render(request, 'eye/stocks.html')

def calendar(request):
    return render(request, 'eye/calendar.html')

def screener(request):
    return render(request, 'eye/screener.html')

def portfolio(request):
    return render(request, 'eye/portfolio.html')


def ticker(request):
    ticker = 'AAPL'
    return render(request, 'eye/ticker.html', {'ticker': ticker})