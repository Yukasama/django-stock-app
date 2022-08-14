import pandas as pd
from datetime import date


class Security():
    
    today = date.today().strftime("%Y-%m-%d")
    
    def __init__(self, symbol):
        self.symbol = symbol
    
    def getPrice(self):
        return self.price


class Stock(Security):
    pass


class Forex(Security):
    pass


class Crypto(Security):
    pass


class Commodity(Security):
    pass