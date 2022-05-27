from django.core.management.base import BaseCommand
from eye.models import Stock, Info, Financial
from eye.stocks import datahandler as dt
import pandas as pd


def DataTransfer(ticker):
    
    try:    
        df = pd.read_csv(f"Data/StockData/{ticker}/info")
        
        city = dt.dataGet(ticker, "city", "info")
        state = dt.dataGet(ticker, "state", "info")
        country = dt.dataGet(ticker, "country", "info")
        address = dt.dataGet(ticker, "address1", "info")
        name = dt.dataGet(ticker, "shortName", "info")
        summary = dt.dataGet(ticker, "longBusinessSummary", "info")
        employees = dt.dataGet(ticker, "fullTimeEmployees", "info")
        sector = dt.dataGet(ticker, "sector", "info")
        industry = dt.dataGet(ticker, "industry", "info")
        exchange = dt.dataGet(ticker, "exchange", "info")
        quoteType = dt.dataGet(ticker, "quoteType", "info")
        currency = dt.dataGet(ticker, "currency", "info")
        phone = dt.dataGet(ticker, "phone", "info")
        website = dt.dataGet(ticker, "website", "info")
        logo = dt.dataGet(ticker, "logo_url", "info")
        
        netIncome = dt.dataGet(ticker, "netIncome")
    except:
        print("Data could'nt be fetched.")
        exit()
        
        
    try:
        symbol = Stock.objects.get(symbol=ticker)
        Stock.objects.delete(symbol=ticker)
        symbol = Stock.objects.create(symbol=ticker)
    except:
        symbol = Stock.objects.create(symbol=ticker)
         
         
    #Info Model   
    try:   
        Info(
            symbol=symbol, 
            city=city, 
            state=state, 
            country=country, 
            address=address, 
            name=name,
            summary=summary,
            employees=employees,
            sector=sector,
            industry=industry,
            exchange=exchange,
            quoteType=quoteType,
            currency=currency,
            phone=phone,
            website=website,
            logo=logo,
        ).save()
        print(f"'{ticker}' Info Model saved.")
    except:
        print(f"'{ticker}' Info Model not saved.")
        
        
    #Cashflow  
    try:
        Financial(
            symbol=symbol,
            ticker=ticker,
            netIncome=netIncome,
        ).save()
        print(f"'{ticker}' Financial Model saved.")
    except:
        print(f"'{ticker}' Financial Model not saved.")      
                

def deleteDuplicates():
    for stock in Stock.objects.all().reverse():
        if Stock.objects.filter(symbol=stock.symbol).count() > 1:
            stock.delete()



class Command(BaseCommand):
    
    def add_arguments(self, parser):
        pass
    
    def handle(sef, *args, **options):
        
        skip = False
        single = True
        
        if (single==False):
            for ticker in dt.tickers_sp500: 
                DataTransfer(ticker)
        else:
            ticker = "AAPL"
            DataTransfer(ticker)
            
        deleteDuplicates()
            
    
        
        
            

    

