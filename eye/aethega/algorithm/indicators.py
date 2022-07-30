import sys
import pandas as pd
import numpy as np
from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(BASE_DIR)
from data.datahandler import dataGet

class Indicator:
    
    def __init__(self, symbol, pattern, timeFrame="daily", period=14, shift=0):
        self.symbol = symbol
        self.pattern = pattern
        self.timeFrame = timeFrame
        self.period = period
        self.shift = shift
    
    def last(self):
        closeLast = self.history().iloc[-1]
        return closeLast
    
    def history(self):
        history = dataGet(self.symbol, 0, "history")
        close = history["Close"]
        return close
    

class iRSI(Indicator):
        
    def history(self):
        history = dataGet(self.symbol, 0, "history")
        closeFrame = pd.DataFrame(history["Close"])
        closePCT = pd.DataFrame(closeFrame.pct_change()).to_numpy()[1:]
        period = self.period
        
        #RSI Calculation
        history_RSI, i = [], -1
        while(i > -300):
            AvgUpArr, AvgDownArr = [], []
            closePCTArr = closePCT[i-period:i]
            for c in closePCTArr:
                AvgUpArr.append(c) if float(c) > 0 else AvgDownArr.append(c)
            #Check for Zeros to avoid Zero Division Error
            AvgUp, AvgDown = sum(AvgUpArr), sum(AvgDownArr)
            if AvgUp == 0: AvgUp = 0.00001
            if AvgDown == 0: AvgDown = 0.00001
            AvgUp = AvgUp / len(AvgUpArr)
            AvgDown = AvgDown / len(AvgDownArr)
            RS = AvgUp / AvgDown
            RSI = 100 - 100 / (1 - RS)
            history_RSI.append(RSI)
            i -= 1
        return max(history_RSI), min(history_RSI)
        
        #Williams %R (WPR)
        # high = history["High"]
        # low = history["Low"]
        
        # if(indicator == "wpr"):
        #     close = close[-1:].squeeze()
        #     highestHigh = max(high[-20:])
        #     lowestLow = min(low[-20:])
        #     WPR = round((highestHigh - close) / (highestHigh - lowestLow) * -100, 3)
        #     return WPR
        
        
        # #Moving Average (MA)
        # if (indicator == "ma"):
            
        #     closePrice = close[-1:].squeeze()
        #     SMA = round(close.rolling(period).mean()[-1:].squeeze(), 3)
            
        #     if (char == "sma"):
        #         return SMA
            
        #     elif (char == "ema"):
        #         #Exponential Moving Average
        #         smoothingConstant = 2 / (period + 1)
        #         EMA = (closePrice - SMA) * smoothingConstant + SMA
        #         return EMA


    
rsi = iRSI("MSFT", "rsi").history()
print(rsi)
