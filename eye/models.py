from django.db import models
from account.models import Account



class Stock(models.Model):
    #Symbol
    symbol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.symbol
    
    
    
class Info(models.Model):
    #Symbol
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10, primary_key=True)
    
    #Address
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    address1 = models.CharField(max_length=300, null=True, blank=True)
    
    #Company Info
    longName = models.CharField(max_length=300, null=True, blank=True)
    longBusinessSummary = models.CharField(max_length=10000, null=True, blank=True)
    fullTimeEmployees = models.FloatField(blank=True, null=True)
    sector = models.CharField(max_length=200, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True)
    exchange = models.CharField(max_length=50, null=True, blank=True)
    quoteType = models.CharField(max_length=50, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    marketCap = models.FloatField(blank=True, null=True)
    recommendationMean = models.FloatField(blank=True, null=True)
    targetMeanPrice = models.FloatField(blank=True, null=True)
    dividendRate = models.FloatField(blank=True, null=True)
    
    #Metrics
    beta = models.FloatField(blank=True, null=True)
    shortRatio = models.FloatField(blank=True, null=True)
    forwardEps = models.FloatField(blank=True, null=True)
    pegRatio = models.FloatField(blank=True, null=True)
    
    #Contact Info
    phone = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)
    logo_url = models.URLField(max_length=500, null=True, blank=True)
    
    #Financials
    period = models.CharField(max_length=5, blank=True, null=True)
    cik = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True, max_length=500)
    finalLink = models.URLField(blank=True, null=True, max_length=500)
    
    
    def __str__(self):
        return self.ticker


    
class Financial(models.Model):
    
    #Symbol Data
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    year = models.IntegerField(db_index=True)
    verification = models.CharField(max_length=15, primary_key=True)
    #Basic Data
    fillingDate = models.DateField(blank=True, null=True)
    #Income Statement
    revenue = models.FloatField(blank=True, null=True)
    costOfRevenue = models.FloatField(blank=True, null=True)
    grossProfit = models.FloatField(blank=True, null=True)
    researchAndDevelopmentExpenses = models.FloatField(blank=True, null=True)
    generalAndAdministrativeExpenses = models.FloatField(blank=True, null=True)
    sellingAndMarketingExpenses = models.FloatField(blank=True, null=True)
    sellingGeneralAndAdministrativeExpenses = models.FloatField(blank=True, null=True)
    otherExpenses = models.FloatField(blank=True, null=True)
    operatingExpenses = models.FloatField(blank=True, null=True)
    costAndExpenses = models.FloatField(blank=True, null=True)
    interestIncome = models.FloatField(blank=True, null=True)
    interestExpense = models.FloatField(blank=True, null=True)
    depreciationAndAmortization = models.FloatField(blank=True, null=True)
    ebitda = models.FloatField(blank=True, null=True)
    ebitdaratio = models.FloatField(blank=True, null=True)
    operatingIncome = models.FloatField(blank=True, null=True)
    totalOtherIncomeExpensesNet = models.FloatField(blank=True, null=True)
    incomeBeforeTax = models.FloatField(blank=True, null=True)
    incomeBeforeTaxRatio = models.FloatField(blank=True, null=True)
    incomeTaxExpense = models.FloatField(blank=True, null=True)
    netIncome = models.FloatField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    epsdiluted = models.FloatField(blank=True, null=True)
    weightedAverageShsOut = models.FloatField(blank=True, null=True)
    weightedAverageShsOutDil = models.FloatField(blank=True, null=True)
    #Balance Sheet
    cashAndCashEquivalents = models.FloatField(blank=True, null=True)
    shortTermInvestments = models.FloatField(blank=True, null=True)
    cashAndShortTermInvestments = models.FloatField(blank=True, null=True)
    netReceivables = models.FloatField(blank=True, null=True)
    inventory = models.FloatField(blank=True, null=True)
    otherCurrentAssets = models.FloatField(blank=True, null=True)
    totalCurrentAssets = models.FloatField(blank=True, null=True)
    propertyPlantEquipmentNet = models.FloatField(blank=True, null=True)
    goodwill = models.FloatField(blank=True, null=True)
    intangibleAssets = models.FloatField(blank=True, null=True)
    goodwillAndIntangibleAssets = models.FloatField(blank=True, null=True)
    longTermInvestments = models.FloatField(blank=True, null=True)
    taxAssets = models.FloatField(blank=True, null=True)
    otherNonCurrentAssets = models.FloatField(blank=True, null=True)
    totalNonCurrentAssets = models.FloatField(blank=True, null=True)
    otherAssets = models.FloatField(blank=True, null=True)
    totalAssets = models.FloatField(blank=True, null=True)
    accountPayables = models.FloatField(blank=True, null=True)
    shortTermDebt = models.FloatField(blank=True, null=True)
    taxPayables = models.FloatField(blank=True, null=True)
    deferredRevenue = models.FloatField(blank=True, null=True)
    otherCurrentLiabilities = models.FloatField(blank=True, null=True)
    totalCurrentLiabilities = models.FloatField(blank=True, null=True)
    longTermDebt = models.FloatField(blank=True, null=True)
    deferredRevenueNonCurrent = models.FloatField(blank=True, null=True)
    deferredTaxLiabilitiesNonCurrent = models.FloatField(blank=True, null=True)
    otherNonCurrentLiabilities = models.FloatField(blank=True, null=True)
    totalNonCurrentLiabilities = models.FloatField(blank=True, null=True)
    otherLiabilities = models.FloatField(blank=True, null=True)
    capitalLeaseObligations = models.FloatField(blank=True, null=True)
    totalLiabilities = models.FloatField(blank=True, null=True)
    preferredStock = models.FloatField(blank=True, null=True)
    commonStock = models.FloatField(blank=True, null=True)
    retainedEarnings = models.FloatField(blank=True, null=True)
    accumulatedOtherComprehensiveIncomeLoss = models.FloatField(blank=True, null=True)
    othertotalStockholdersEquity = models.FloatField(blank=True, null=True)
    totalStockholdersEquity = models.FloatField(blank=True, null=True)
    totalLiabilitiesAndStockholdersEquity = models.FloatField(blank=True, null=True)
    minorityInterest = models.FloatField(blank=True, null=True)
    totalEquity = models.FloatField(blank=True, null=True)
    totalLiabilitiesAndTotalEquity = models.FloatField(blank=True, null=True)
    totalInvestments = models.FloatField(blank=True, null=True)
    totalDebt = models.FloatField(blank=True, null=True)
    netDebt = models.FloatField(blank=True, null=True)
    #Cashflow
    deferredIncomeTax = models.FloatField(blank=True, null=True)
    stockBasedCompensation = models.FloatField(blank=True, null=True)
    changeInWorkingCapital = models.FloatField(blank=True, null=True)
    accountsReceivables = models.FloatField(blank=True, null=True)
    accountsPayables = models.FloatField(blank=True, null=True)
    otherWorkingCapital = models.FloatField(blank=True, null=True)
    otherNonCashItems = models.FloatField(blank=True, null=True)
    netCashProvidedByOperatingActivities = models.FloatField(blank=True, null=True)
    investmentsInPropertyPlantAndEquipment = models.FloatField(blank=True, null=True)
    acquisitionsNet = models.FloatField(blank=True, null=True)
    purchasesOfInvestments = models.FloatField(blank=True, null=True)
    salesMaturitiesOfInvestments = models.FloatField(blank=True, null=True)
    otherInvestingActivites = models.FloatField(blank=True, null=True)
    netCashUsedForInvestingActivites = models.FloatField(blank=True, null=True)
    debtRepayment = models.FloatField(blank=True, null=True)
    commonStockIssued = models.FloatField(blank=True, null=True)
    commonStockRepurchased = models.FloatField(blank=True, null=True)
    dividendsPaid = models.FloatField(blank=True, null=True)
    otherFinancingActivites = models.FloatField(blank=True, null=True)
    netCashUsedProvidedByFinancingActivities = models.FloatField(blank=True, null=True)
    effectOfForexChangesOnCash = models.FloatField(blank=True, null=True)
    netChangeInCash = models.FloatField(blank=True, null=True)
    cashAtEndOfPeriod = models.FloatField(blank=True, null=True)
    cashAtBeginningOfPeriod = models.FloatField(blank=True, null=True)
    operatingCashFlow = models.FloatField(blank=True, null=True)
    capitalExpenditure = models.FloatField(blank=True, null=True)
    freeCashFlow = models.FloatField(blank=True, null=True)
    #Key Metrics
    revenuePerShare = models.FloatField(blank=True, null=True)
    netIncomePerShare = models.FloatField(blank=True, null=True)
    operatingCashFlowPerShare = models.FloatField(blank=True, null=True)
    freeCashFlowPerShare = models.FloatField(blank=True, null=True)
    cashPerShare = models.FloatField(blank=True, null=True)
    bookValuePerShare = models.FloatField(blank=True, null=True)
    tangibleBookValuePerShare = models.FloatField(blank=True, null=True)
    shareholdersEquityPerShare = models.FloatField(blank=True, null=True)
    interestDebtPerShare = models.FloatField(blank=True, null=True)
    marketCap = models.FloatField(blank=True, null=True)
    enterpriseValue = models.FloatField(blank=True, null=True)
    peRatio = models.FloatField(blank=True, null=True)
    priceToSalesRatio = models.FloatField(blank=True, null=True)
    pocfratio = models.FloatField(blank=True, null=True)
    pfcfRatio = models.FloatField(blank=True, null=True)
    pbRatio = models.FloatField(blank=True, null=True)
    evToSales = models.FloatField(blank=True, null=True)
    enterpriseValueOverEBITDA = models.FloatField(blank=True, null=True)
    evToOperatingCashFlow = models.FloatField(blank=True, null=True)
    evToFreeCashFlow = models.FloatField(blank=True, null=True)
    earningsYield = models.FloatField(blank=True, null=True)
    freeCashFlowYield = models.FloatField(blank=True, null=True)
    debtToEquity = models.FloatField(blank=True, null=True)
    debtToAssets = models.FloatField(blank=True, null=True)
    netDebtToEBITDA = models.FloatField(blank=True, null=True)
    currentRatio = models.FloatField(blank=True, null=True)
    interestCoverage = models.FloatField(blank=True, null=True)
    incomeQuality = models.FloatField(blank=True, null=True)
    dividendYield = models.FloatField(blank=True, null=True)
    payoutRatio = models.FloatField(blank=True, null=True)
    salesGeneralAndAdministrativeToRevenue = models.FloatField(blank=True, null=True)
    researchAndDdevelopementToRevenue = models.FloatField(blank=True, null=True)
    intangiblesToTotalAssets = models.FloatField(blank=True, null=True)
    capexToOperatingCashFlow = models.FloatField(blank=True, null=True)
    capexToRevenue = models.FloatField(blank=True, null=True)
    capexToDepreciation = models.FloatField(blank=True, null=True)
    stockBasedCompensationToRevenue = models.FloatField(blank=True, null=True)
    grahamNumber = models.FloatField(blank=True, null=True)
    roic = models.FloatField(blank=True, null=True)
    returnOnTangibleAssets = models.FloatField(blank=True, null=True)
    grahamNetNet = models.FloatField(blank=True, null=True)
    workingCapital = models.FloatField(blank=True, null=True)
    tangibleAssetValue = models.FloatField(blank=True, null=True)
    netCurrentAssetValue = models.FloatField(blank=True, null=True)
    investedCapital = models.FloatField(blank=True, null=True)
    averageReceivables = models.FloatField(blank=True, null=True)
    averagePayables = models.FloatField(blank=True, null=True)
    averageInventory = models.FloatField(blank=True, null=True)
    daysSalesOutstanding = models.FloatField(blank=True, null=True)
    daysPayablesOutstanding = models.FloatField(blank=True, null=True)
    daysOfInventoryOnHand = models.FloatField(blank=True, null=True)
    receivablesTurnover = models.FloatField(blank=True, null=True)
    payablesTurnover = models.FloatField(blank=True, null=True)
    inventoryTurnover = models.FloatField(blank=True, null=True)
    capexPerShare = models.FloatField(blank=True, null=True)
    #Financial Ratios
    quickRatio = models.FloatField(blank=True, null=True)
    cashRatio = models.FloatField(blank=True, null=True)
    daysOfSalesOutstanding = models.FloatField(blank=True, null=True)
    daysOfInventoryOutstanding = models.FloatField(blank=True, null=True)
    operatingCycle = models.FloatField(blank=True, null=True)
    daysOfPayablesOutstanding = models.FloatField(blank=True, null=True)
    cashConversionCycle = models.FloatField(blank=True, null=True)
    grossProfitMargin = models.FloatField(blank=True, null=True)
    operatingProfitMargin = models.FloatField(blank=True, null=True)
    pretaxProfitMargin = models.FloatField(blank=True, null=True)
    netProfitMargin = models.FloatField(blank=True, null=True)
    effectiveTaxRate = models.FloatField(blank=True, null=True)
    returnOnAssets = models.FloatField(blank=True, null=True)
    returnOnEquity = models.FloatField(blank=True, null=True)
    returnOnCapitalEmployed = models.FloatField(blank=True, null=True)
    netIncomePerEBT = models.FloatField(blank=True, null=True)
    ebtPerEbit = models.FloatField(blank=True, null=True)
    ebitPerRevenue = models.FloatField(blank=True, null=True)
    debtRatio = models.FloatField(blank=True, null=True)
    debtEquityRatio = models.FloatField(blank=True, null=True)
    longTermDebtToCapitalization = models.FloatField(blank=True, null=True)
    totalDebtToCapitalization = models.FloatField(blank=True, null=True)
    cashFlowToDebtRatio = models.FloatField(blank=True, null=True)
    companyEquityMultiplier = models.FloatField(blank=True, null=True)
    fixedAssetTurnover = models.FloatField(blank=True, null=True)
    assetTurnover = models.FloatField(blank=True, null=True)
    operatingCashFlowSalesRatio = models.FloatField(blank=True, null=True)
    freeCashFlowOperatingCashFlowRatio = models.FloatField(blank=True, null=True)
    cashFlowCoverageRatios = models.FloatField(blank=True, null=True)
    shortTermCoverageRatios = models.FloatField(blank=True, null=True)
    capitalExpenditureCoverageRatio = models.FloatField(blank=True, null=True)
    dividendPaidAndCapexCoverageRatio = models.FloatField(blank=True, null=True)
    priceEarningsToGrowthRatio = models.FloatField(blank=True, null=True)
    enterpriseValueMultiple = models.FloatField(blank=True, null=True)
    priceFairValue = models.FloatField(blank=True, null=True)
    
    #Discounted Cash Flow
    date = models.DateField(blank=True, null=True)
    stockPrice  = models.FloatField(blank=True, null=True)
    DCF = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.verification
    
    
    
class ShortFinancial(models.Model):
    #Symbol Data
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    year = models.IntegerField(db_index=True)
    verification = models.CharField(max_length=15, primary_key=True)
    
    #Income Statement
    revenue = models.FloatField(blank=True, null=True)
    
    #Key Metrics
    eps = models.FloatField(blank=True, null=True)
    marketCap = models.FloatField(blank=True, null=True)
    enterpriseValue = models.FloatField(blank=True, null=True)
    peRatio = models.FloatField(blank=True, null=True)
    priceToSalesRatio = models.FloatField(blank=True, null=True)
    pfcfRatio = models.FloatField(blank=True, null=True)
    pbRatio = models.FloatField(blank=True, null=True)
    debtToEquity = models.FloatField(blank=True, null=True)
    debtToAssets = models.FloatField(blank=True, null=True)
    netDebtToEBITDA = models.FloatField(blank=True, null=True)
    currentRatio = models.FloatField(blank=True, null=True)
    dividendYield = models.FloatField(blank=True, null=True)
    payoutRatio = models.FloatField(blank=True, null=True)
    roic = models.FloatField(blank=True, null=True)
    roe = models.FloatField(blank=True, null=True)
    
    #Financial Ratios
    quickRatio = models.FloatField(blank=True, null=True)
    cashRatio = models.FloatField(blank=True, null=True)
    grossProfitMargin = models.FloatField(blank=True, null=True)
    operatingProfitMargin = models.FloatField(blank=True, null=True)
    netProfitMargin = models.FloatField(blank=True, null=True)
    debtRatio = models.FloatField(blank=True, null=True)
    assetTurnover = models.FloatField(blank=True, null=True)
    
    revenueGrowth = models.FloatField(blank=True, null=True)
    debtGrowth = models.FloatField(blank=True, null=True)
    DCF = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.verification



class History(models.Model):
    
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    date = models.DateField(null=True, blank=True)
    openPrice = models.FloatField(null=True, blank=True)
    highPrice = models.FloatField(null=True, blank=True)
    lowPrice = models.FloatField(null=True, blank=True)
    closePrice = models.FloatField(null=True, blank=True)
    closePct = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.ticker
    
 
 
 
class EconomicData(models.Model):
    interestRate = models.FloatField(null=True, blank=True)
    spread10Y2Y = models.FloatField(null=True, blank=True)
    
 
    
    
class Portfolio(models.Model):
    
    #User Based
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    
    #Stocks
    stocks = models.ManyToManyField(Stock, related_name="stocks", blank=True)
    
    #Additional
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}-{self.name}'
    
    

        
