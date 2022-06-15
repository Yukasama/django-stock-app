from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from eye.models import Stock, Info, Financial, Portfolio
from eye.stocks import datahandler as dt
from eye.forms import PortfolioForm




def stocks(request):
    return render(request, 'eye/stocks.html')


def calendar(request):
    return render(request, 'eye/calendar.html')


def news(request):
    return render(request, 'eye/news.html')


def education(request):
    return render(request, 'eye/education.html')


def screener(request):
    return render(request, 'eye/screener.html')


def portfolio(request):
    form = PortfolioForm(initial={"host": request.user})
    #Check for Create Form
    if (request.method == 'POST'):
        form = PortfolioForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("portfolio")
    exists = False
    portfolios = Portfolio.objects.filter()
    if (portfolios.exists()): exists = True
    data = {
        'form': form,
        'portfolios': portfolios,
        'exists': exists,
    }
    return render(request, 'eye/portfolio.html', data)


def symbol(request, symbol):
    symbol = Stock.objects.get(symbol=symbol)
    info = Info.objects.filter(symbol=symbol)
    #Data
    mode = "dark" 
    infoList = ["ticker", "city", "state", "country", "address", "name", "summary", 
                "employees", "sector", "industry", "exchange", "quoteType", "currency", 
                "phone", "website", "logo", "period", "cik", "link", "finalLink"]
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