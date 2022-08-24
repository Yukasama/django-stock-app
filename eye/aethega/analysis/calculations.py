from algorithm.indicators import *
import pandas as pd, numpy as np
# from .models import Financial
import statistics as stat
from data.datahandler import *


"""
Description:
The Calculator Class is used to calculate different Stock Based Values that
can be used in eg. Website Projects or Machine Learning. The Calculator calculates,
for instance, the FA-R (Fundamental Analysis Rating) or TA-R (Technical Analysis Rating).
Arguments:
Symbol: Ticker of Stock Symbol
"""
class Calculator():
    
    def __init__(self, symbol):
        self.symbol = symbol


    def TAR(self, equalWeight=False, mean=False):
        def calc(symbol):
            
            #Test if Ticker exists
            try: date, openPrice, high, low, close, volume = getHistory(symbol)
            except: 
                print(f"'{symbol}' Ticker doesn't exist")
                return None
            
            #Variables for Calculation
            rMonth, rYear, rYear3 = 23, 261, 783
            lenClose = len(close)
            closeLast = close[-1:].squeeze()
            
            tarFactors = {
                "high52": round(closeLast / max(high[-rYear:]) - 1, 3),
                "low52": round(closeLast / min(low[-rYear:]) - 1, 3),
                "return30d": close[lenClose - 1] / close[lenClose - rMonth] - 1,
                "return1y": close[lenClose - 1] / close[lenClose - rYear] - 1,
                "return3y": close[lenClose - 1] / close[lenClose -rYear3] - 1,
                "fibonacci1y": round(closeLast / ((max(high[-rYear:]) + min(low[-rYear:])) / 2), 3),
                "fibonacci3y": round(closeLast / ((max(high[-rYear3:]) + min(low[-rYear3:])) / 2), 3),
                "sma50": closeLast / MA("MSFT", 50).last()[0] - 1,
                "sma100": closeLast / MA("MSFT", 100).last()[0] - 1,
                "sma200": closeLast / MA("MSFT", 200).last()[0] - 1,       
            }

            weight = {
                "high52": 1.1, "low52": 1, "return30d": 1, "return1y": 1.15,
                "return3y": 1, "fibonacci1y": 1, "fibonacci3y": 1, "sma50": 1.15,
                "sma100": 1, "sma200": 1,
            }
            #Best Value
            rangeHigh = {
                "high52": -0.5, "low52": 0.1, "return30d": -0.15, "return1y": -0.05,
                "return3y": 0.02, "fibonacci1y": -0.1, "fibonacci3y": 0, "sma50": -0.3,
                "sma100": -0.25, "sma200": -0.2,
            }
            #Worst Value
            rangeLow = {
                "high52": 0.025, "low52": 0.7, "return30d": 0.15, "return1y": 0.35, 
                "return3y": 0.8, "fibonacci1y": 1, "fibonacci3y": 2, "sma50": 0.2,
                "sma100": 0.25, "sma200": 0.3,
            }
            
            #Loop through TAR Factors
            TAR_array = []
            for key, value in tarFactors.items():
                
                #Recalculate TAR Values to 0 - 1
                tempTAR = ((value - rangeLow[key]) / (rangeHigh[key] - rangeLow[key]))
                
                #Weighing of values applied
                if equalWeight == False:
                    tempTAR = tempTAR * weight[key]
                    
                #Setting overflowing Values to Limits
                if (tempTAR < 0): tempTAR = 0
                elif (tempTAR > 1): tempTAR = 1
                
                #Append finished TAR Value to TAR Array
                TAR_array.append(tempTAR)
                
            #Average of TAR Values
            TAR = round(stat.mean(TAR_array), 3)
            return TAR
                
    
        if(type(self.symbol) == str):
            return calc(self.symbol)
            
        elif(len(self.symbol) > 1 or type(self.symbol[0]) == str and len(self.symbol) == 1):
            symbol_array, tar_array = [], []
            for s in self.symbol:
                TAR = calc(s)
                                
                if not (TAR == None):
                    tar_array.append(TAR)
                    symbol_array.append(s)        

            if (mean == True):
                result = stat.mean(tar_array)
            elif (mean == False):
                result = pd.DataFrame({
                    "Symbol": symbol_array,
                    "TAR": tar_array,
                })
            return result
        
        
    def FAR(weightedAverage=True, sectorBalancing=False, timeFluence=True, averageDeviation=False, allowForecast=False):
        def valueFunction(value):
            
            #Value Register
            #Returns: Value => [Worst, Best, Limit]
            values = {
                "peRatio": [-20, 15, 50]
            }
            
            return values[value]

        print(valueFunction("peRatio"))
        return 0.8

print(Calculator("AAL").FAR())