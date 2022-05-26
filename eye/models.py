from django.db import models



class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.symbol
    
    
    
class Info(models.Model):
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    
    #Address
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    
    #Company Info
    name = models.CharField(max_length=300)
    summary = models.CharField(max_length=10000)
    employees = models.IntegerField()
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    exchange = models.CharField(max_length=50)
    quoteType = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    
    #Contact Info
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=300)
    logo = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.name
    
    
    
class Cashflow(models.Model):
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    netIncome = models.IntegerField(blank=True, null=True)
    
    
    def __str__(self):
        return self.ticker
    
