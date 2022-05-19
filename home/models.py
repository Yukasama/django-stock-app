from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=1000)
    
    
class StockFundamentals(models.Model): 
    peRatio = models.IntegerField(max_length=20)
    pegRatio = models.IntegerField(max_length=20)
    
    
    