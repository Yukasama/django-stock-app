import pandas as pd
from datetime import date
from orders import *


class Account():
    
    balance = 10000
    securities = pd.DataFrame(columns=["Symbol", "Shares", "Price", "Direction", "Operation", "Execution Date", "P/L"])
    executionDate = date.today().strftime('%Y-%m-%d')
    
    def showBalance(self):
        print(f"Account Balance: {self.balance}")
        
    def orderExecute(self, order):
        recipient = "Securities" if order.operation == "BUY" else "Balance"
        self.balanceTransfer(recipient, order.amount)
        self.securityPass(order)
            
    def balanceTransfer(self, recipient, amount):
        if recipient == "Securities":
            if self.balance - amount > 0:
                self.balance += amount
            else:
                print("Balance is too low.")
        elif recipient == "Securities":
            pass
        
    def securityPass(self, order):
        self.securities.append(
            order.symbol, 
            order.amount, 
            order.price, 
            order.direction, 
            order.operation, 
            executionDate, 
            100,
        )
    
    def sellItAll(self):
        for s in self.securities:
            amount = s["Amount"]
            Order(s, amount)
    
        
order = Order("MSFT", 100, 100, "LONG", "BUY")
Account().orderExecute(order)

print(Account().securities)