from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from eye.models import Stock, Info, Financial, Portfolio
from eye.stocks import datahandler as dt
from eye.forms import PortfolioForm
from django.core import serializers
import pandas as pd




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
    marginLabels = []
    grossMarginV, operatingMarginV, profitMarginV = [], [], []
    data = {
        'mode': "dark",
        'marginLabels': marginLabels,
        'grossMarginV': grossMarginV,
        'operatingMarginV': operatingMarginV,
        'profitMarginV': profitMarginV,
    }
    #Create Auto-Generated Dict from Info Data Model
    info = Info.objects.filter(symbol=symbol).values()[0]
    for key, value in info.items():
        data[key] = value
    #Create Auto-Generated Dict from Financial Data Model
    for year in range(2014, 2022):
        financial = Financial.objects.filter(symbol=symbol, year=year).values()[0]
        marginLabels.append(year)
        for key, value in financial.items():
            key = f'{key}{year}'
            data[key] = value
            if(key == f"grossProfitMargin{year}"):
                grossMarginV.append(value)
            elif(key == f"operatingProfitMargin{year}"):
                operatingMarginV.append(value)
            elif(key == f"netProfitMargin{year}"):
                profitMarginV.append(value)
            

    return render(request, 'eye/symbol.html', data)