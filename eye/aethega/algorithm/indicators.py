#region Libraries
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import talib as ta
from data.datahandler import *
#endregion

class Indicator():
        
    def __init__(self, symbol, period=14, timeFrame="daily", shift=0):
        self.symbol = symbol
        self.period = period
        self.timeFrame = timeFrame
        self.shift = shift
        self.date, self.open, self.high, self.low, self.close, self.volume = DataHandler(self.symbol).getHistory()
        
    def calc(self):
        result = pd.Series(self.close)
        return result
    
    def last(self):
        result = self.calc()
        return [result.iloc[-1][0], result.iloc[-2][0], result.iloc[-3][0]]

    def history(self, start, end):
        date = pd.DataFrame(self.date)
        close = pd.DataFrame(self.close)
        result = date.join(close)
        return result["Close"]
    
    def graph(self):
        date = pd.DataFrame(self.date)
        close = pd.DataFrame(self.close)
        result = date.join(close)
        #offshore = result.iloc[start, end]
        return pd.Series(result["Date"]).to_list(), pd.Series(result["Close"]).to_list()
    
    
class RSI(Indicator):
    
    def calc(self):
        result = pd.Series(ta.RSI(self.close, self.period)).dropna()
        return result    
    
    
class MA(Indicator):
    
    def __init__(self, symbol, period=14, config="sma", timeFrame="daily", shift=0):
        self.config = config
        super(MA, self).__init__(symbol, period, timeFrame, shift)
            
    def calc(self):
        maPatterns = {
            "sma": pd.DataFrame(ta.SMA(self.close, self.period)).dropna(),
            "ema": pd.DataFrame(ta.EMA(self.close, self.period)).dropna(),
            "wma": pd.DataFrame(ta.WMA(self.close, self.period)).dropna(),
            "dema": pd.DataFrame(ta.DEMA(self.close, self.period)).dropna(),
            "tema": pd.DataFrame(ta.TEMA(self.close, self.period)).dropna(),
            "trima": pd.DataFrame(ta.TRIMA(self.close, self.period)).dropna(),
        }
        result = maPatterns.get(self.config)
        return result
    
    
class WPR(Indicator):
            
    def calc(self):
        result = pd.Series(ta.WILLR(self.high, self.low, self.close, self.period)).dropna()
        return result


class MACD(Indicator):
        
    def __init__(self, symbol, period=12, slowperiod=26, signalperiod=9, timeFrame="daily", shift=0):
        self.slowperiod = slowperiod
        self.signalperiod = signalperiod
        super(MACD, self).__init__(symbol, period, timeFrame, shift)
            
    def calc(self):
        result1, result2, result3 = ta.MACD(self.close, self.fastperiod, self.slowperiod, self.signalperiod)
        return result1, result2, result3
        
    def last(self):
        result1, result2, result3 = self.calc()
        result1 = [result1.iloc[-1], result1.iloc[-2], result1.iloc[-3]]
        result2 = [result2.iloc[-1], result2.iloc[-2], result2.iloc[-3]]
        result3 = [result3.iloc[-1], result3.iloc[-2], result3.iloc[-3]]
        return pd.DataFrame([result1, result2, result3], columns=["Fast MA", "Slow MA", "Signal MA"])
    
    def history(self):
        result1, result2, result3 = self.calc()
        return pd.DataFrame([result1, result2, result3], columns=["Fast MA", "Slow MA", "Signal MA"])
    
    
class ATR(Indicator):
            
    def calc(self):
        result = pd.Series(ta.ATR(self.high, self.low, self.close, self.period)).dropna()
        return result


class OBV(Indicator):
        
    def calc(self):
        result = pd.Series(ta.OBV(self.close, self.volume))
        return result


class ADOSC(Indicator):
    
    def __init__(symbol, period=3, slowperiod=10, timeFrame="daily", shift=0):
        self.slowperiod = slowperiod
        super(ADOSC, self).__init__(symbol, period, timeFrame, shift)
        
    def calc(self):
        result = pd.Series(ta.ADOSC(self.high, self.low, self.close, self.volume, self.period, self.slowperiod))
        return result

