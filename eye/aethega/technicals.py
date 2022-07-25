
#Dependencies
import datahandler as data
import pandas as pd


#-------------------------------------------------------------------------------------------------------------------

class Stock:
    
    def __init__(self, symbol):
        pass
    

def Indicator(ticker, indicator, period=14, shift=0, char="sma"):
    
    #Function Globals
    history = data.dataGet(ticker, 0, fileName="history")
    close = history["Close"]
    lenClose = len(close)
    
    
    #Relative Strength Index (RSI)
    if(indicator == "rsi"):
        averageGain, averageLoss, day = 0, 0, -1 - shift
        while(day >= period - period * 2):
            closeDiff = close[lenClose + day] - close[lenClose + day - 1]
            if (closeDiff >= 0): averageGain += closeDiff
            elif (closeDiff < 0): averageLoss -= closeDiff
            day -= 1
        RSI = 100 - 100 / (1 + averageGain / averageLoss)
        return RSI
    
    
    #Williams %R (WPR)
    high = history["High"]
    low = history["Low"]
    
    if(indicator == "wpr"):
        close = close[-1:].squeeze()
        highestHigh = max(high[-20:])
        lowestLow = min(low[-20:])
        WPR = round((highestHigh - close) / (highestHigh - lowestLow) * -100, 3)
        return WPR
    
    
    #Moving Average (MA)
    if (indicator == "ma"):
        
        closePrice = close[-1:].squeeze()
        SMA = round(close.rolling(period).mean()[-1:].squeeze(), 3)
        
        if (char == "sma"):
            return SMA
        
        elif (char == "ema"):
            #Exponential Moving Average
            smoothingConstant = 2 / (period + 1)
            EMA = (closePrice - SMA) * smoothingConstant + SMA
            return EMA
        
      
    
def singleTAR(tickerAsArray, progress):
    
    #Function Globals
    try: 
        history = data.dataGet(tickerAsArray, 0, fileName="history")
        close = history["Close"]
        lenClose = len(close)
        closePrice = close[-1:].squeeze()
        high = history["High"]
        low = history["Low"]
    except: 
        print(f"'{tickerAsArray}' Ticker doesn't exist")
    rMonth, rYear, rYear3 = 23, 261, 783
    
    #Technical Factors
    try:
        high52Price = round(max(high[-rYear:]) - 1, 3)
        low52Price = round(min(low[-rYear:]) - 1, 3)
        high52 = round(closePrice / max(high[-rYear:]) - 1, 3)
        low52 = round(closePrice / min(low[-rYear:]) - 1, 3)
        return30d = close[lenClose - 1] / close[lenClose - rMonth] - 1
        return1y = close[lenClose - 1] / close[lenClose - rYear] - 1
        return3y = close[lenClose - 1] / close[lenClose -rYear3] - 1
        fibonacci1y = round(closePrice / ((high52Price + low52Price) / 2), 3)
        fibonacci3y = round(closePrice / ((max(high[-rYear3:]) + min(low[-rYear3:])) / 2), 3)
        
        #Technical Indicators
        sma50 = closePrice / Indicator(tickerAsArray, "ma", 50) - 1
        sma100 = closePrice / Indicator(tickerAsArray, "ma", 100) - 1
        sma200 = closePrice / Indicator(tickerAsArray, "ma", 200) - 1
       
        #Factor Weighing
        weight = {
            high52: 1.1, low52: 1, return30d: 1, return1y: 1.15,
            return3y: 1, fibonacci1y: 1, fibonacci3y: 1, sma50: 1.15,
            sma100: 1, sma200: 1,
        }
        #Best Value
        rangeHigh = {
            high52: -0.5, low52: 0.1, return30d: -0.15, return1y: -0.05,
            return3y: 0.02, fibonacci1y: -0.1, fibonacci3y: 0, sma50: -0.3,
            sma100: -0.25, sma200: -0.2,
        }
        #Worst Value
        rangeLow = {
            high52: 0.025, low52: 0.7, return30d: 0.15, return1y: 0.35, 
            return3y: 0.8, fibonacci1y: 1, fibonacci3y: 2, sma50: 0.2,
            sma100: 0.25, sma200: 0.3,
        }
    
    
        #Calculate TAR
        TAR_array = []
        
        #All measurements which should influence TAR
        measures = [high52, low52, return30d, return1y, return3y, fibonacci1y, 
                    fibonacci3y, sma50, sma100, sma200]
        
        #Loop through measures
        for m in measures:
            newValue = (((m - rangeLow[m]) * 1) / (rangeHigh[m] - rangeLow[m]))
            TAR_value = newValue * weight[m]
            #Setting overflowing Values to Limits
            if (TAR_value <= 0): TAR_value = 0
            elif (TAR_value >= 1): TAR_value = 1
            TAR_array.append(TAR_value)
        TAR = sum(TAR_array) / len(TAR_array)
        return TAR
    except:
        if (progress == True): print(f"'{tickerAsArray}: skipped.'")
        return None



def TAR(tickerAsArray, operator=False, progress=False, addition=0):
    
    if(operator == True):
        return singleTAR(tickerAsArray, progress)
    
    elif(operator == False):
        tar_array, ticker_array, sector_array, addition_array = [], [], [], []
        additionValue = 0
        for t in tickerAsArray:
            tar = singleTAR(t, progress)
            sector = data.dataGet(t, "sector", "info")
            if (addition != 0):
                additionValue = data.dataGet(t, addition, "info")
            
            if (progress == True): print(f"{t}: {tar}")
            
            if not (tar == None):
                tar_array.append(tar)
                ticker_array.append(t)
                sector_array.append(sector)
                addition_array.append(additionValue)           

        result = pd.DataFrame(
            {"Ticker": ticker_array,
             "Sector": sector_array,
             "TAR": tar_array,
             addition: addition_array,
             })
        return result
    
    
def TARresearch(output, command):
    
    #General Mean of TAR   
    if(command == "mean"):
        result = output["TAR"].mean()
        
    #Each Sector Mean of TAR
    elif(command == "sectormean"):
        result = output.groupby("Sector", as_index=False)["TAR"].mean()
    return result