#region LIBRARIES
import time, os, math
from datetime import datetime as dt
import yfinance as yf
import pandas as pd, numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from collections import defaultdict
from statistics import mean, median
import json
from eye.models import Stock, Info, Financial
from core.utils import listAverage
#import pandas_datareader.nasdaq_trader as nas
#from pandas_datareader import wb
#import yahoo_fin.stock_info as si
#import FundamentalAnalysis as fa
#endregion

T_SP500 = pd.read_csv("Data/SymbolData/S&P500")["0"] #S&P 500 Ticker List
T_DAX40 = pd.read_csv("Data/SymbolData/DAX40")["0"] #DAX Ticker List
TICKERS = pd.concat([T_SP500, T_DAX40], axis=0)
TODAY = dt.today()

"""

"""
class Formatter():
    
    def isNull(self, element):
        return True if(element == None or element == "" or element == 0) else False
    
    
    def dataConstruct(self, data, construct):
        if(construct == "floatArray"):
            tempResult = pd.DataFrame(data).to_numpy()[0]
            tempResult1 = tempResult.tolist()
            tempResult1.reverse()
            tempResult1.pop()
            result = [float(x) for x in tempResult1]
        
        elif(construct == "normal"):
            tempResult = pd.DataFrame(data).to_numpy()[0]
            result = ",".join(map(str, tempResult))
            
            if (result == "0.0"):
                result = 0
            #If result == integer
            elif(result.isdigit()):
                if(result == 0.0):
                    result = int(result)
                else:
                    result = float(result)
            
        return result


class DataHandler():
    
    #GLOBALS
    API_KEY = "1451443e6ac73f65840c60adab375261" #ApiKey for FundamentalAnalysis
    REQUEST_COOLER = 181
    blackList = ["BBWI", "BF-B", "CARR", "CEG", "CTXS"]
    
    def __init__(self, symbol):
        self.symbol = symbol


    def fundamentalData(self, skipMode=True):
        for t in self.symbol:
            #If File exists, skip Ticker
            if ((os.path.exists(f"Data/StockData/{t}/income_statement") and skipMode == True) or t in self.blackList):
                print(f"'{t}' Fundamental Data was skipped.")
                continue
            
            try:
                #File Collection for For Loop
                csvDict = {
                    "income_statement": fa.income_statement(t, self.API_KEY),
                    "balance_sheet": fa.balance_sheet_statement(t, self.API_KEY),
                    "cash_flow": fa.cash_flow_statement(t, self.API_KEY),
                    "discounted_cash_flow": fa.discounted_cash_flow(t, self.API_KEY),
                    "financial_ratios": fa.financial_ratios(t, self.API_KEY),
                    "key_metrics": fa.key_metrics(t, self.API_KEY),    
                }
                    
                #Convert to CSV Files
                for key, value in csvDict: 
                    value.to_csv(f"Data/StockData/{t}/{key}")
                
                print(f"'{t}' Fundamental Data was pushed successfully!")
                
            except:
                print(f"Cooling down requests for 5 minutes..")
                time.sleep(self.REQUEST_COOLER + 120)
                continue
                    
        #If multiple Tickers get pushed, execute Sleep Timer
        time.sleep(self.REQUEST_COOLER) if (len(ticker) > 1) else exit()
        

    def economicData(self):
        startDate = "1900/01/01"
        
        #Get Economic Data
        csvDict = {
            "interestRate": web.DataReader("DFF", "fred", startDate, TODAY),
            "spread10Y2Y": web.DataReader("T10Y2Y", "fred", startDate, TODAY),
        }

        #Convert to CSV Files
        for key, value in csvDict:
            value.to_csv(f"Data/EconomicData/{key}")

        print(f"Economic Data was pushed successfully!")


    def dataPush(self, single=0, pushRate=5, skipMode=True):
            
        #Count Errors => End Loop if Limit Reach
        request_error = 0
        
        for t in self.symbol:
            
            #Defining Variables
            ticker = yf.Ticker(t)
            
            if (skipMode == True):
                if (os.path.exists(f"Data/StockData/{t}/info") and 
                os.path.exists(f"Data/StockData/{t}/major_holders")):
                    print(f"'{t}' was skipped.")
                    continue
                            
            #Get Data from Yahoo Finance
            if(single == "history"):
                history = ticker.history(period="max")
                os.makedirs(f"Data/StockData/{t}", exist_ok=True)
                try: 
                    history.to_csv(f"Data/StockData/{t}/history")
                    print(f"'{t}' History File pushed successfully.")
                    time.sleep(pushRate)
                    continue
                except: 
                    print(f"'{t}' History File skipped.")
                    continue
                
            
            info, calendar, actions, analysis = ticker.info, ticker.calendar, ticker.actions, ticker.analysis
            try: 
                news = ticker.news
                news = pd.DataFrame.from_dict(news)
            except:
                news = 0
                pass
            recommendations, sustainability, major_holders = ticker.recommendations, ticker.sustainability, ticker.major_holders
            institutional_holders, history = ticker.institutional_holders, ticker.history(period="max")
            
            #Preparing Data for Push
            df_info = pd.DataFrame.from_dict(info)
            t_info, v_info = [], []
            for data in df_info: #Pushing Info into Arrays
                t_info.append(data)
                v_info.append(info[data])
            info = pd.DataFrame(v_info, t_info) #Create new DataFrame from Arrays

            csvFiles = [info, news, calendar, actions, analysis, recommendations, 
                        sustainability, major_holders, institutional_holders, history]
            csvStrings = ["info", "news", "calendar", "actions", "analysis", "recommendations",
                        "sustainability", "major_holders", "institutional_holders", "history"]                        
                
            #Create Stock Folder if doesn't exist
            os.makedirs(f"Data/StockData/{t}", exist_ok=True)
            
            #Data Push
            for c, s in zip(csvFiles, csvStrings):
                try: 
                    c.to_csv(f"Data/StockData/{t}/{s}")
                    print(f"'{t}' Data was pushed successfully!")
                except: 
                    print(f"'{t}' {s.capitalize()} File was skipped")
                    pass
            
            
            #Check if requests get rejected
            if(request_error >= 10):
                print(f"Cooling down requests for 3 minutes..")
                time.sleep(self.REQUEST_COOLER)
                request_error = 0
                pass
            if(request_error >= 15):
                print(f"Ending Loop due to RequestErrorOverflow.")
                exit()         
            time.sleep(pushRate)
        

    def deleteFiles(self, fileName):
        
        for t in self.symbol:
            try: os.remove(f"Data/StockData/{t}/{fileName}")
            except: 
                print(f"There was no file found for ticker '{t}'")
                continue
        

    def copyRows(self, action="models", output=False):
        
        ticker = "AAPL"
        
        #Financial Statements
        income_statement = pd.read_csv(f"Data/StockData/{ticker}/income_statement").iloc[:,0]
        balance_sheet = pd.read_csv(f"Data/StockData/{ticker}/balance_sheet").iloc[:,0]
        cash_flow = pd.read_csv(f"Data/StockData/{ticker}/cash_flow").iloc[:,0]
        key_metrics = pd.read_csv(f"Data/StockData/{ticker}/key_metrics").iloc[:,0]
        financial_ratios = pd.read_csv(f"Data/StockData/{ticker}/financial_ratios").iloc[:,0]
        financial_statement_growth = pd.read_csv(f"Data/StockData/{ticker}/financial_statement_growth").iloc[:,0]
        discounted_cash_flow = pd.read_csv(f"Data/StockData/{ticker}/discounted_cash_flow").iloc[:,0]
        
        names = pd.concat([income_statement, balance_sheet, cash_flow, key_metrics,
                financial_ratios, financial_statement_growth, discounted_cash_flow])
        names = names.drop_duplicates(keep='first')
        blackList = ["reportedCurrency", "acceptedDate", "calendarYear", "priceEarningsRatio", "priceBookValueRatio",
                    "priceToBookRatio", "ptbRatio", "priceToFreeCashFlowsRatio",
                    "priceCashFlowRatio", "returnOnEquity", "grossProfitRatio", "operatingIncomeRatio",
                    "incomeBeforeTaxRatio", "netIncomeRatio", "priceSalesRatio", "dividendPayoutRatio",
                    "priceToOperatingCashFlowsRatio", "period", "cik", "link", "finalLink", "roe"]
        
        if(action == "models"):
            for name in names:
                print(f'{name} = models.IntegerField(blank=True, null=True)')
                
        elif(action == "modelInsert"):
            array = []
            for name in names:
                if name in blackList: continue
                array.append(name)
                print(f'{name} = findict["{name}"],')
            print(len(array))  
                
        elif(action == "viewModel"):
            for name in names:
                print(f"'{name}': financial.{name},")
            
        elif(action == "array"):
            array = []
            for name in names:
                if name in blackList:
                    continue
                elif (name == "Stock Price"):
                    name = "stockPrice"
                array.append(name)
            print(array)
            
            if (output == True):
                newData = pd.DataFrame(array)
                newData.to_csv("Data/SymbolData/FinData")
                print(len(newData))
                

    def dataGet(self, value, fileName=0, year=str(TODAY.year - 1), output=False):
        
        def calc(value, fileName, year, output):
            t = self.symbol.upper()
            
            #Error Checking
            if (Formatter().isNull(t)):
                raise ValueError("Ticker Element is Null")
            elif not type(t) == str:
                raise ValueError("Ticker has to be <str>")
            if (value == 0 and fileName != 0):
                result = pd.read_csv(f'Data/StockData/{t}/{fileName}')
                return result
            
            #Return single value from File
            elif (value != 0 and fileName != 0):
                df = pd.read_csv(f'Data/StockData/{t}/{fileName}')
                #Data Getting for Info, Calendar, Sustainability & History
                if (fileName == "info" or fileName == "calendar"):
                    try: df_new = df.loc[df["Unnamed: 0"] == value]["0"]
                    except: df_new = df.loc[df["Unnamed: 0"] == value]["Value"]
                elif (fileName == "sustainability"):
                    df_new = df.loc[df["2022-2"] == value]["0"]           
                elif (fileName == "history"):
                    return df[value]
                else: 
                    print("There's no such file/value.")
                result = Formatter().dataConstruct(df_new, "normal")
                return result
            
            elif (fileName == 0):
                files = ["income_statement", "balance_sheet", "cash_flow", "financial_ratios",
                            "key_metrics", "discounted_cash_flow"]
                tickerFrame = pd.DataFrame()
                
                if (value == "all"):
                    if not os.path.exists(f'Data/StockData/{t}/income_statement'):
                        return pd.DataFrame()
                    else: 
                        for f in files:
                            df = pd.read_csv(f'Data/StockData/{t}/{f}')
                            tickerFrame = pd.concat([tickerFrame, df])
                        tickerFrame = tickerFrame.drop_duplicates(keep="first")
                        return tickerFrame
                else:
                    for f in files:
                        try:
                            df = pd.read_csv(f'Data/StockData/{t}/{f}')
                            if (year == "ALL"): 
                                df_new = df.loc[df["Unnamed: 0"] == value]
                                result = Formatter().dataConstruct(df_new, "floatArray")
                            elif (year == str(TODAY.year - 1)):
                                try: df_new = df.loc[df["Unnamed: 0"] == value][str(TODAY.year)]
                                except: df_new = df.loc[df["Unnamed: 0"] == value][str(TODAY.year - 1)]
                                result = Formatter().dataConstruct(df_new, "normal")
                            else:
                                df_new = df.loc[df["Unnamed: 0"] == value][str(year)]
                                result = Formatter().dataConstruct(df_new, "normal")
                            return result
                        except: continue

        if len(self.symbol) == 1 or type(self.symbol) == str:
            try: 
                result = calc(value, fileName, year, output)
                return result
            except Exception as e: print("Error: " + str(e))
        
        elif len(self.symbol) > 1:
            dataArray, tickerArray = [], []
            for t in ticker: 
                result = calc(value, fileName, year, output)
                dataArray.append(result)
                tickerArray.append(t)    
            
            #Output File if checked true
            if (output == True):
                datadf = pd.DataFrame(dataArray, tickerArray)
                datadf.to_csv(f"Data/ComparisonData/{value}")
                
            return dataArray



    #Returns Open, High, Low, Close, Volume Array
    def getHistory(self):
        history = self.dataGet(0, "history")
        return (history["Date"], history["Open"], history["High"],
                history["Low"], history["Close"], history["Volume"])
        
        
    #Returns a Dictionary with all Data from Stock
    def stockData(self):
    
        #Data Dictionary for storing Stock Data
        data, years = defaultdict(list), []
        stock = Stock.objects.get(symbol=self.symbol)
        
        #Create Auto-Generated Dictionary from Financial Model
        for year in range(2015, 2022):
            financial = Financial.objects.filter(symbol=stock, year=year).values()[0]
            years.append(year)
            for key, value in financial.items():
                keyZero = f'{key}_M'
                if (key == "grossProfitMargin" or key == "operatingProfitMargin" or key == "netProfitMargin"): 
                    data[key].append(round(value * 100, 2)) if value != None else data[key].append(0)
                else: 
                    try: data[key].append(round(value, 3)) if value != None else data[key].append(0)
                    except: data[key].append(value) if value != None else data[key].append(0)
                try: data[keyZero].append(int(value / 1000000))
                except: data[keyZero].append(value) if value != None else 0
                
        #Create Auto-Generated Dict from Info Data Model
        info = Info.objects.filter(symbol=stock).values()[0]
        for key, value in info.items(): data[key] = value

        #List of 5 Competitors
        competitors = Info.objects.filter(sector=data["sector"])\
        .order_by("marketCap").exclude(symbol=stock)[:5]
        data["competitors"] = competitors
        
        data["years"] = years
        data["dividendYieldChecker"] = [i + i for i in data["dividendYield"]]
        desc = data["longBusinessSummary"].split(".")
        data["descShort"] = desc[0]+"." + desc[1]+"." + desc[2]+"."
        try: data["recommendationMean"] = round(1 - (data["recommendationMean"] - 1) / (5 - 1), 3)
        except: data["recommendationMean"] = "N/A"
                
        return data
      
      
class DataModels():
        
  #Calculates the Sector Average of all Values with 3 Steps (Dictionaries)
  def stockAverage(self, filter="sector"):
    
    #Dictionary => Filter: [Stocks]
    stocksFiltered = {}
    for symbol in T_SP500:
      try:
        info = DataHandler(symbol).dataGet(filter, "info")
        stocksFiltered[info].append(symbol)
      except:
        stocksFiltered[info] = [symbol]
          
    #Dictionary => Filter_Metric: List of Lists
    averagesFiltered = {}
    for key, symbolList in stocksFiltered.items():
      try:
        for symbol in symbolList:
          try:
            stockData = DataHandler(symbol).stockData()
            for metric, value in stockData.items():
              if "_M" in metric: continue
              try:
                averagesFiltered[f"{key}_{metric}"].append(value)
              except:
                averagesFiltered[f"{key}_{metric}"] = [value]
          except:
            pass   
      except:
        pass
    
    #Final Dictionary => Filter_Metric: Value Array
    results = {}
    for key, listOfLists in averagesFiltered.items():
        try:
            results[key] = listAverage(listOfLists)
        except:
            pass
        
    return results     

