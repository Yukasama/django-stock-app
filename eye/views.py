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
    info = Info.objects.filter(symbol=symbol)
  
    #Data
    mode = "dark" 
    infoList = ["city", "state", "country", "address", "name", "summary", "employees",
                "sector", "industry", "exchange", "quoteType", "currency", "phone",
                "website", "logo", "period", "cik", "link", "finalLink", "ticker"]
    findata = dt.findata
    
    data = {
        'mode': mode,
    }
    
    
    for item in infoList:
        key = f'{item}'
        value = info.values_list(item, flat=True).first()
        data[key] = value
            
    for year in range(2021, 2022):
        financial = Financial.objects.filter(symbol=symbol, year=year)
        for fin in findata:
            key = f'{fin}{year}'
            value = financial.values_list(fin, flat=True).first()
            data[key] = value
    

    return render(request, 'eye/symbol.html', data)