from django.shortcuts import render
from eye.models import Stock, Info, Financial


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
    info = Info.objects.get(symbol=symbol)
    financial = Financial.objects.get(symbol=symbol)
    
    mode = "dark"
    
    stock = {
        'symbol': symbol,
        
        'city': info.city,
        'state': info.state,
        'country': info.country,
        'address': info.address,
        
        'name': info.name,
        'summary': info.summary,
        'employees': info.employees,
        'sector': info.sector,
        'industry': info.industry,
        'exchange': info.exchange,
        'quoteType': info.quoteType,
        'currency': info.currency,
        
        'phone': info.phone,
        'website': info.website,
        'logo': info.logo,
        
        'mode': mode,
    }
    return render(request, 'eye/symbol.html', stock)