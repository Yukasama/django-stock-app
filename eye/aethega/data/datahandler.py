#region LIBRARIES
import time, os, math
from datetime import datetime as dt
import yfinance as yf
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
#import pandas_datareader.nasdaq_trader as nas
#from pandas_datareader import wb
#import yahoo_fin.stock_info as si
#import FundamentalAnalysis as fa
#endregion

#GLOBALS
API_KEY = "1451443e6ac73f65840c60adab375261" #ApiKey for FundamentalAnalysis
T_SP500 = pd.read_csv("Data/SymbolData/S&P500")["0"] #S&P 500 Ticker List
T_DAX40 = pd.read_csv("Data/SymbolData/DAX40")["0"] #DAX Ticker List
TICKERS = pd.concat([T_SP500, T_DAX40], axis=0)
REQUEST_COOLER = 181
TODAY = dt.today()


#-------------------------------------------------------------------------------------------------------------------

def isNull(element):
    return True if(element == None or element == "" or element == 0) else False
        

#def dataRoutine():
#    fundamentalData(T_SP500)


#-------------------------------------------------------------------------------------------------------------------


def fundamentalData(tickerAsArray, skipMode=True):
    
    blackList = ["BBWI", "BF-B", "CARR", "CEG", "CTXS"]

    for t in tickerAsArray:

        #If File exists, skip Ticker
        if ((os.path.exists(f"Data/StockData/{t}/income_statement")) or t in blackList):
            print(f"'{t}' Fundamental Data was skipped.")
            continue
        
        try:
            #File Collection for For Loop
            csvDict = {
                "income_statement": fa.income_statement(t, API_KEY),
                "balance_sheet": fa.balance_sheet_statement(t, API_KEY),
                "cash_flow": fa.cash_flow_statement(t, API_KEY),
                "discounted_cash_flow": fa.discounted_cash_flow(t, API_KEY),
                "financial_ratios": fa.financial_ratios(t, API_KEY),
                "key_metrics": fa.key_metrics(t, API_KEY),    
            }
                
            #Convert to CSV Files
            for key, value in csvDict: 
                value.to_csv(f"Data/StockData/{t}/{key}")
            
            print(f"'{t}' Fundamental Data was pushed successfully!")
            
        except:
            print(f"Cooling down requests for 5 minutes..")
            time.sleep(REQUEST_COOLER + 120)
            continue
                
        #If multiple Tickers get pushed, execute Sleep Timer
        time.sleep(REQUEST_COOLER) if (len(tickerAsArray) > 1) else exit()
        
         
#-------------------------------------------------------------------------------------------------------------------


def economicData():
    
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

    
#-------------------------------------------------------------------------------------------------------------------


def dataPush(tickerAsArray, pushRate=5, skipMode=True, single=0):
        
    #Count Errors => End Loop if Limit Reach
    request_error = 0
    
    for t in tickerAsArray:
        
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
            time.sleep(REQUEST_COOLER)
            request_error = 0
            pass
        if(request_error >= 15):
            print(f"Ending Loop due to RequestErrorOverflow.")
            exit()         
        time.sleep(pushRate)
        

#-------------------------------------------------------------------------------------------------------------------


def deleteFiles(tickerAsArray, fileName):
    
    for t in tickerAsArray:
        try: os.remove(f"Data/StockData/{t}/{fileName}")
        except: 
            print(f"There was no file found for ticker '{t}'")
            continue
        


def copyRows(action="models", output=False):
    
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
                
# copyRows("modelInsert")


#-------------------------------------------------------------------------------------------------------------------

#Get pushed Data

def dataConstruct(data, construct):
    
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



def dataGetTemp(ticker, value, fileName=0, year=str(TODAY.year - 1)):
    
    t = ticker.upper()
    
    #Error Checking
    if (isNull(t)):
        raise ValueError("Ticker Element is Null")
    elif not type(ticker) == str:
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
        result = dataConstruct(df_new, "normal")
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
                        result = dataConstruct(df_new, "floatArray")
                    elif (year == str(TODAY.year - 1)):
                        try: df_new = df.loc[df["Unnamed: 0"] == value][str(TODAY.year)]
                        except: df_new = df.loc[df["Unnamed: 0"] == value][str(TODAY.year - 1)]
                        result = dataConstruct(df_new, "normal")
                    else:
                        df_new = df.loc[df["Unnamed: 0"] == value][str(year)]
                        result = dataConstruct(df_new, "normal")
                    return result
                except: continue




def dataGet(tickerAsArray, value, fileName=0, year=str(TODAY.year - 1), operator=True, output=False):

    if (operator == True):
        try: 
            result = dataGetTemp(tickerAsArray, value, fileName, year)
            return result
        except Exception as e: print("Error: " + str(e))
    
    elif (operator == False):
        dataArray, tickerArray = [], []
        for t in tickerAsArray: 
             result = dataGetTemp(t, value, fileName)
             dataArray.append(result)
             tickerArray.append(t)    
        
        #Output File if checked true
        if(output==True and len(tickerAsArray) > 1):
            datadf = pd.DataFrame(dataArray, tickerArray)
            datadf.to_csv(f"Data/ComparisonData/{value}")
            
        #If theres only one ticker, print the result
        if (len(tickerAsArray) == 1): return result
        elif (len(tickerAsArray) > 1): return dataArray




#Returns Open, High, Low, Close, Volume Array
def getHistory(symbol):
    history = dataGet(symbol, 0, "history")
    return (history["Date"], history["Open"], history["High"],
            history["Low"], history["Close"], history["Volume"])
