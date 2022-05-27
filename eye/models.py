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
    website = models.URLField(max_length=300)
    logo = models.URLField(max_length=500)
    
    
    def __str__(self):
        return self.name
    
    
    
class Financial(models.Model):
    
    #Symbol Data
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    
    #Income Statement
    fillingDate = models.DateField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    costOfRevenue = models.IntegerField(blank=True, null=True)
    grossProfit = models.IntegerField(blank=True, null=True)
    grossProfitRatio = models.IntegerField(blank=True, null=True)
    researchAndDevelopmentExpenses = models.IntegerField(blank=True, null=True)
    generalAndAdministrativeExpenses = models.IntegerField(blank=True, null=True)
    sellingAndMarketingExpenses = models.IntegerField(blank=True, null=True)
    sellingGeneralAndAdministrativeExpenses = models.IntegerField(blank=True, null=True)
    otherExpenses = models.IntegerField(blank=True, null=True)
    operatingExpenses = models.IntegerField(blank=True, null=True)
    costAndExpenses = models.IntegerField(blank=True, null=True)
    interestIncome = models.IntegerField(blank=True, null=True)
    interestExpense = models.IntegerField(blank=True, null=True)
    depreciationAndAmortization = models.IntegerField(blank=True, null=True)
    ebitda = models.IntegerField(blank=True, null=True)
    ebitdaratio = models.IntegerField(blank=True, null=True)
    operatingIncome = models.IntegerField(blank=True, null=True)
    operatingIncomeRatio = models.IntegerField(blank=True, null=True)
    totalOtherIncomeExpensesNet = models.IntegerField(blank=True, null=True)
    incomeBeforeTax = models.IntegerField(blank=True, null=True)
    incomeBeforeTaxRatio = models.IntegerField(blank=True, null=True)
    incomeTaxExpense = models.IntegerField(blank=True, null=True)
    netIncome = models.IntegerField(blank=True, null=True)
    netIncomeRatio = models.IntegerField(blank=True, null=True)
    eps = models.IntegerField(blank=True, null=True)
    epsdiluted = models.IntegerField(blank=True, null=True)
    weightedAverageShsOut = models.IntegerField(blank=True, null=True)
    weightedAverageShsOutDil = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True, max_length=500)
    finalLink = models.URLField(blank=True, null=True, max_length=500)
    
    #Balance Sheet
    
    
    
    def __str__(self):
        return self.ticker
    
