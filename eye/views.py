from django.shortcuts import render
from eye.models import Stock, Info, Financial
from eye.stocks import datahandler as dt



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
    #financial = Financial.objects.filter(symbol=symbol)
  
    mode = "dark" 
     
    data = {
        'mode': mode,
    }
    
    findata = dt.findata
    
    for year in range(2017, 2022):
        financial = Financial.objects.filter(symbol=symbol, year=year)
        for fin in findata:
            key = f'{fin}{year}'
            value = financial.values_list(fin, flat=True).first()
            data[key] = value
    

    
    return render(request, 'eye/symbol.html', data)