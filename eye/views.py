from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from eye.models import Stock, Info, Financial, Portfolio, ShortFinancial, History
from eye.aethega.data.datahandler import *
from eye.aethega.analysis.calculator import Calculator
from eye.aethega.algorithm import indicators as ic
from eye.forms import PortfolioForm
from django.core import serializers
import pandas as pd
from django.core.mail import send_mail
import json

import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)





def stocks(request):
    page = "stocks"
    yearLabels = []
    data = defaultdict(list)
    
    for symbol in Stock.objects.all():
        try:
            symbol = Stock.objects.get(symbol=symbol)
            #Create Auto-Generated Dictionary from Financial Model
            # for year in range(2014, 2022):
            #     financial = ShortFinancial.objects.filter(symbol=symbol, year=year).values()[0]
            #     yearLabels.append(year)
            #     for key, value in financial.items():
            #         key = f'{symbol}_{key}'
            #         yearKey = f'{symbol}_{key}{year}'
            #         keyZero = f'{symbol}_{key}{year}_M'
            #         data[key].append(value)
            #         data[yearKey] = value
            #Create Auto-Generated Dict from Info Data Model
            info = Info.objects.filter(symbol=symbol).values()[0]
            for key, value in info.items():
                key = f'{symbol}_{key}'
                data[key] = value
        except: print(f"Error: '{symbol}' failed to load.")
        
    data["yearLabels"] = yearLabels
    data["page"] = page
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
    page = "symbol"
    data = DataHandler(symbol).stockData()

    #Extra Fields
    data["mode"] = "dark"
    data["page"] = page
    
    #EYE Ratings
    data["TAR"] = json.dumps(Calculator(data["ticker"]).TAR())
    data["FAR"] = json.dumps(Calculator(data["ticker"]).FAR())
    data["EYE"] = round((float(data["FAR"]) + float(data["TAR"])) / 2, 3)
        
    return render(request, 'eye/symbol.html', data)



def portfolio(request):
    page = "portfolio"
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
        'page': page,
    }
    for p in portfolios:
        pass
        
    
    return render(request, 'eye/portfolio.html', data)



def algorithm(request):
    rsi = ic.RSI("MSFT").history(1, 1)
    wpr = ic.WPR("MSFT").history(1, 1)
    date, close = ic.Indicator("MSFT").graph()
    date = [json.loads(json.dumps(d)) for d in date]
        
    data = {
        "date": date,
        "close": close,
    }
    
    return render(request, "eye/algorithm.html", data)



def neuralNetwork(request):
    
    return render(request, "eye/neuralnetwork.html")