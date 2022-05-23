from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.symbol
    
    
class StockInfo(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class StockCashFlow(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    
    metric = models.CharField(max_length=200)
    y2016 = models.IntegerField()
    
