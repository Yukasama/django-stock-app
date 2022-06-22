from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from eye.models import Stock, Info, Financial, Portfolio, ShortFinancial
from eye.stocks import datahandler as dt
from eye.forms import PortfolioForm
from django.core import serializers
import pandas as pd
from collections import defaultdict
from django.core.mail import send_mail




def stocks(request):
    yearLabels = []
    data = defaultdict(list)
    
    for symbol in Stock.objects.all():
        try:
            symbol = Stock.objects.get(symbol=symbol)
            #Create Auto-Generated Dictionary from Financial Model
            for year in range(2014, 2022):
                financial = ShortFinancial.objects.filter(symbol=symbol, year=year).values()[0]
                yearLabels.append(year)
                for key, value in financial.items():
                    key = f'{symbol}_{key}'
                    yearKey = f'{symbol}_{key}{year}'
                    data[key].append(value)
                    data[yearKey] = value
            #Create Auto-Generated Dict from Info Data Model
            info = Info.objects.filter(symbol=symbol).values()[0]
            for key, value in info.items():
                key = f'{symbol}_{key}'
                data[key] = value
        except: print(f"Error: '{symbol}' failed to load.")
        
    data["yearLabels"] = yearLabels
    return render(request, 'eye/stocks.html')



def calendar(request):
    return render(request, 'eye/calendar.html')



def news(request):
    return render(request, 'eye/news.html')



def education(request):
    return render(request, 'eye/education.html')



def screener(request):
    return render(request, 'eye/screener.html')



def symbol(request, symbol):
    symbol = Stock.objects.get(symbol=symbol)
    data, yearLabels = defaultdict(list), []
    #Create Auto-Generated Dictionary from Financial Model
    for year in range(2014, 2022):
        financial = Financial.objects.filter(symbol=symbol, year=year).values()[0]
        yearLabels.append(year)
        for key, value in financial.items():
            yearKey = f'{key}{year}'
            data[key].append(value)
            data[yearKey] = value
    #Create Auto-Generated Dict from Info Data Model
    info = Info.objects.filter(symbol=symbol).values()[0]
    for key, value in info.items(): data[key] = value    
    
    data["yearLabels"], data["mode"] = yearLabels, "dark"

    return render(request, 'eye/symbol.html', data)



def portfolio(request):
    form = PortfolioForm()
    #Check for Create Form
    if (request.method == 'POST'):
        form = PortfolioForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("portfolio")
    portfolios = Portfolio.objects.filter(user=request.user)
    exists = True if portfolios.exists() else False
    data = {
        'form': form,
        'portfolios': portfolios,
        'exists': exists,
    }
    for p in portfolios:
        pass
        
    
    return render(request, 'eye/portfolio.html', data)