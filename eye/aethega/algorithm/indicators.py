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
    

class RSI(Indicator):
        
    def history(self):
        history = dataGet(self.symbol, 0, "history")
        closeFrame = pd.DataFrame(history["Close"])
        closePCT = pd.DataFrame(closeFrame.pct_change()).to_numpy()
        closePCT = closePCT[1:]
        period = self.period
        
        #RSI Calculation
        history_RSI = []
        i=-1
        print(len(closePCT[i:i-period]), closePCT[i:i-period])
        AvgUpArr, AvgDownArr = [], []
        
        for c in closePCT[i:i-period]:
            if c == 0: continue
            AvgUpArr.append(c) if float(c) > 0 else AvgDownArr.append(c)
        AvgUp = sum(AvgUpArr) / len(AvgUpArr)
        AvgDown = sum(AvgDownArr) / len(AvgDownArr)
        print(AvgUp, AvgDown)
        RS = AvgUp / AvgDown
        RSI = 100 - 100 / (1 + RS)
        history_RSI.append(RSI)
        i -= 1
        print(i)
        print(RSI)


    
rsi = RSI("MSFT", "rsi").history()
print(rsi)
