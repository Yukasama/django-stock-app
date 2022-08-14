from datetime import date
import random

class Order():
    
    orderBook = []
    today = date.today().strftime('%Y-%m-%d')
    
    def __init__(self, symbol, amount, price, direction, operation):
        self.symbol = symbol
        self.amount = amount
        self.price = price
        self.direction = direction
        self.operation = operation
        
    def order(self, symbol, amount, price, direction, operation):
        self.orderLog()
        print(f"'{symbol}' Order executed")
    
    def orderLog(self):
        orderBook = self.orderBook
        orderNumber = self.orderNumber()
        orderDetails = ({
            "Order Number": orderNumber,
            "Symbol": self.symbol,
            "Amount": self.amount,
            "Execution Price": self.price,
            "Order Direction": self.direction,
            "Order Operation": self.operation,
            "Execution Date": today,
        })
        orderBook.append(orderDetails)
        return orderDetails
    
    def orderNumber(self):
        randomNums = random.randint(10000000, 99999999)
        orderNumber = f"#{randomNums}"
        return orderNumber
        
    
class Buy(Order):
    
    operation = "BUY"
    
    def __init__(self, symbol, amount, price, direction):
        super(Buy, self).__init__(symbol, amount, price, direction, self.operation)
        self.order(symbol, amount, price, direction, self.operation)
        
           
class Close(Order):
    
    operation = "SELL"
    
    def __init__(self, symbol, amount, price, direction, operation):
        self.order(symbol, amount, price, direction, self.operation)
        
        
class ClosePartial(Order):
    
    operation = "SELL"
    
    def __init__(self, symbol, amount, price, direction):
        self.order(symbol, amount, price, direction, self.operation)


Buy("MSFT", 100, 100, "LONG")
print(Order.orderBook)