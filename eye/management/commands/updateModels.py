from django.core.management.base import BaseCommand
from eye.models import Stock, Info, Financial, ShortFinancial
from eye.stocks import datahandler as dt
import pandas as pd
import datetime



def DataTransfer(ticker):
    
    #Duplicate Handling  
    try:
        Stock.objects.delete(symbol=ticker)
        symbol = Stock.objects.create(symbol=ticker)
    except:
        symbol = Stock.objects.create(symbol=ticker)
        
    for stock in Stock.objects.all():
        if Stock.objects.filter(symbol=stock.symbol).count() > 1:
            stock.delete()
            
            
    try:    
        df = pd.read_csv(f"Data/StockData/{ticker}/info")
        
        city = dt.dataGet(ticker, "city", "info")
        state = dt.dataGet(ticker, "state", "info")
        country = dt.dataGet(ticker, "country", "info")
        address = dt.dataGet(ticker, "address1", "info")
        name = dt.dataGet(ticker, "longName", "info")
        summary = dt.dataGet(ticker, "longBusinessSummary", "info")
        employees = dt.dataGet(ticker, "fullTimeEmployees", "info")
        sector = dt.dataGet(ticker, "sector", "info")
        industry = dt.dataGet(ticker, "industry", "info")
        exchange = dt.dataGet(ticker, "exchange", "info")
        quoteType = dt.dataGet(ticker, "quoteType", "info")
        currency = dt.dataGet(ticker, "currency", "info")
        phone = dt.dataGet(ticker, "phone", "info")
        website = dt.dataGet(ticker, "website", "info")
        logo = dt.dataGet(ticker, "logo_url", "info")
        period = dt.dataGet(ticker, "period", 0, str(2021))
        cik = dt.dataGet(ticker, "cik", 0, str(2021))
        link = dt.dataGet(ticker, "link", 0, str(2021))
        finalLink = dt.dataGet(ticker, "finalLink", 0, str(2021))
    except:
        print("Data could'nt be fetched.")
        exit()
    
    
    #Financial Data
    for year in range(2014, 2022):
        #Basic Data
        fillingDate = dt.dataGet(ticker, "fillingDate", 0, str(year))
        #Income Statement
        revenue = dt.dataGet(ticker, "revenue", 0, str(year))
        costOfRevenue = dt.dataGet(ticker, "costOfRevenue", 0, str(year))
        grossProfit = dt.dataGet(ticker, "grossProfit", 0, str(year))
        researchAndDevelopmentExpenses = dt.dataGet(ticker, "researchAndDevelopmentExpenses", 0, str(year))
        generalAndAdministrativeExpenses = dt.dataGet(ticker, "generalAndAdministrativeExpenses", 0, str(year))
        sellingAndMarketingExpenses = dt.dataGet(ticker, "sellingAndMarketingExpenses", 0, str(year))
        sellingGeneralAndAdministrativeExpenses = dt.dataGet(ticker, "sellingGeneralAndAdministrativeExpenses", 0, str(year))
        otherExpenses = dt.dataGet(ticker, "otherExpenses", 0, str(year))
        operatingExpenses = dt.dataGet(ticker, "operatingExpenses", 0, str(year))
        costAndExpenses = dt.dataGet(ticker, "costAndExpenses", 0, str(year))
        interestIncome = dt.dataGet(ticker, "interestIncome", 0, str(year))
        interestExpense = dt.dataGet(ticker, "interestExpense", 0, str(year))
        depreciationAndAmortization = dt.dataGet(ticker, "depreciationAndAmortization", 0, str(year))
        ebitda = dt.dataGet(ticker, "ebitda", 0, str(year))
        ebitdaratio = dt.dataGet(ticker, "ebitdaratio", 0, str(year))
        operatingIncome = dt.dataGet(ticker, "operatingIncome", 0, str(year))
        totalOtherIncomeExpensesNet = dt.dataGet(ticker, "totalOtherIncomeExpensesNet", 0, str(year))
        incomeBeforeTax = dt.dataGet(ticker, "incomeBeforeTax", 0, str(year))
        incomeTaxExpense = dt.dataGet(ticker, "incomeTaxExpense", 0, str(year))
        netIncome = dt.dataGet(ticker, "netIncome", 0, str(year))
        try: eps = round(float(dt.dataGet(ticker, "eps", 0, str(year))), 2)
        except: eps = dt.dataGet(ticker, "eps", 0, str(year))
        epsdiluted = dt.dataGet(ticker, "epsdiluted", 0, str(year))
        weightedAverageShsOut = dt.dataGet(ticker, "weightedAverageShsOut", 0, str(year))
        weightedAverageShsOutDil = dt.dataGet(ticker, "weightedAverageShsOutDil", 0, str(year))
        #Balance Sheet
        cashAndCashEquivalents = dt.dataGet(ticker, "cashAndCashEquivalents", 0, str(year))
        shortTermInvestments = dt.dataGet(ticker, "shortTermInvestments", 0, str(year))
        cashAndShortTermInvestments = dt.dataGet(ticker, "cashAndShortTermInvestments", 0, str(year))
        netReceivables = dt.dataGet(ticker, "netReceivables", 0, str(year))
        inventory = dt.dataGet(ticker, "inventory", 0, str(year))
        otherCurrentAssets = dt.dataGet(ticker, "otherCurrentAssets", 0, str(year))
        totalCurrentAssets = dt.dataGet(ticker, "totalCurrentAssets", 0, str(year))
        propertyPlantEquipmentNet = dt.dataGet(ticker, "propertyPlantEquipmentNet", 0, str(year))
        goodwill = dt.dataGet(ticker, "goodwill", 0, str(year))
        intangibleAssets = dt.dataGet(ticker, "intangibleAssets", 0, str(year))
        goodwillAndIntangibleAssets = dt.dataGet(ticker, "goodwillAndIntangibleAssets", 0, str(year))
        longTermInvestments = dt.dataGet(ticker, "longTermInvestments", 0, str(year))
        taxAssets = dt.dataGet(ticker, "taxAssets", 0, str(year))
        otherNonCurrentAssets = dt.dataGet(ticker, "otherNonCurrentAssets", 0, str(year))
        totalNonCurrentAssets = dt.dataGet(ticker, "totalNonCurrentAssets", 0, str(year))
        otherAssets = dt.dataGet(ticker, "otherAssets", 0, str(year))
        totalAssets = dt.dataGet(ticker, "totalAssets", 0, str(year))
        accountPayables = dt.dataGet(ticker, "accountPayables", 0, str(year))
        shortTermDebt = dt.dataGet(ticker, "shortTermDebt", 0, str(year))
        taxPayables = dt.dataGet(ticker, "taxPayables", 0, str(year))
        deferredRevenue = dt.dataGet(ticker, "deferredRevenue", 0, str(year))
        otherCurrentLiabilities = dt.dataGet(ticker, "otherCurrentLiabilities", 0, str(year))
        totalCurrentLiabilities = dt.dataGet(ticker, "totalCurrentLiabilities", 0, str(year))
        longTermDebt = dt.dataGet(ticker, "longTermDebt", 0, str(year))
        deferredRevenueNonCurrent = dt.dataGet(ticker, "deferredRevenueNonCurrent", 0, str(year))
        deferredTaxLiabilitiesNonCurrent = dt.dataGet(ticker, "deferredTaxLiabilitiesNonCurrent", 0, str(year))
        otherNonCurrentLiabilities = dt.dataGet(ticker, "otherNonCurrentLiabilities", 0, str(year))
        totalNonCurrentLiabilities = dt.dataGet(ticker, "totalNonCurrentLiabilities", 0, str(year))
        otherLiabilities = dt.dataGet(ticker, "otherLiabilities", 0, str(year))
        capitalLeaseObligations = dt.dataGet(ticker, "capitalLeaseObligations", 0, str(year))
        totalLiabilities = dt.dataGet(ticker, "totalLiabilities", 0, str(year))
        preferredStock = dt.dataGet(ticker, "preferredStock", 0, str(year))
        commonStock = dt.dataGet(ticker, "commonStock", 0, str(year))
        retainedEarnings = dt.dataGet(ticker, "retainedEarnings", 0, str(year))
        accumulatedOtherComprehensiveIncomeLoss = dt.dataGet(ticker, "accumulatedOtherComprehensiveIncomeLoss", 0, str(year))
        othertotalStockholdersEquity = dt.dataGet(ticker, "othertotalStockholdersEquity", 0, str(year))
        totalStockholdersEquity = dt.dataGet(ticker, "totalStockholdersEquity", 0, str(year))
        totalLiabilitiesAndStockholdersEquity = dt.dataGet(ticker, "totalLiabilitiesAndStockholdersEquity", 0, str(year))
        minorityInterest = dt.dataGet(ticker, "minorityInterest", 0, str(year))
        totalEquity = dt.dataGet(ticker, "totalEquity", 0, str(year))
        totalLiabilitiesAndTotalEquity = dt.dataGet(ticker, "totalLiabilitiesAndTotalEquity", 0, str(year))
        totalInvestments = dt.dataGet(ticker, "totalInvestments", 0, str(year))
        totalDebt = dt.dataGet(ticker, "totalDebt", 0, str(year))
        netDebt = dt.dataGet(ticker, "netDebt", 0, str(year))
        #CashFlow
        deferredIncomeTax = dt.dataGet(ticker, "deferredIncomeTax", 0, str(year))
        stockBasedCompensation = dt.dataGet(ticker, "stockBasedCompensation", 0, str(year))
        changeInWorkingCapital = dt.dataGet(ticker, "changeInWorkingCapital", 0, str(year))
        accountsReceivables = dt.dataGet(ticker, "accountsReceivables", 0, str(year))
        accountsPayables = dt.dataGet(ticker, "accountsPayables", 0, str(year))
        otherWorkingCapital = dt.dataGet(ticker, "otherWorkingCapital", 0, str(year))
        otherNonCashItems = dt.dataGet(ticker, "otherNonCashItems", 0, str(year))
        netCashProvidedByOperatingActivities = dt.dataGet(ticker, "netCashProvidedByOperatingActivities", 0, str(year))
        investmentsInPropertyPlantAndEquipment = dt.dataGet(ticker, "investmentsInPropertyPlantAndEquipment", 0, str(year))
        acquisitionsNet = dt.dataGet(ticker, "acquisitionsNet", 0, str(year))
        purchasesOfInvestments = dt.dataGet(ticker, "purchasesOfInvestments", 0, str(year))
        salesMaturitiesOfInvestments = dt.dataGet(ticker, "salesMaturitiesOfInvestments", 0, str(year))
        otherInvestingActivites = dt.dataGet(ticker, "otherInvestingActivites", 0, str(year))
        netCashUsedForInvestingActivites = dt.dataGet(ticker, "netCashUsedForInvestingActivites", 0, str(year))
        debtRepayment = dt.dataGet(ticker, "debtRepayment", 0, str(year))
        commonStockIssued = dt.dataGet(ticker, "commonStockIssued", 0, str(year))
        commonStockRepurchased = dt.dataGet(ticker, "commonStockRepurchased", 0, str(year))
        dividendsPaid = dt.dataGet(ticker, "dividendsPaid", 0, str(year))
        otherFinancingActivites = dt.dataGet(ticker, "otherFinancingActivites", 0, str(year))
        netCashUsedProvidedByFinancingActivities = dt.dataGet(ticker, "netCashUsedProvidedByFinancingActivities", 0, str(year))
        effectOfForexChangesOnCash = dt.dataGet(ticker, "effectOfForexChangesOnCash", 0, str(year))
        netChangeInCash = dt.dataGet(ticker, "netChangeInCash", 0, str(year))
        cashAtEndOfPeriod = dt.dataGet(ticker, "cashAtEndOfPeriod", 0, str(year))
        cashAtBeginningOfPeriod = dt.dataGet(ticker, "cashAtBeginningOfPeriod", 0, str(year))
        operatingCashFlow = dt.dataGet(ticker, "operatingCashFlow", 0, str(year))
        capitalExpenditure = dt.dataGet(ticker, "capitalExpenditure", 0, str(year))
        freeCashFlow = dt.dataGet(ticker, "freeCashFlow", 0, str(year))
        #Key Metrics
        revenuePerShare = dt.dataGet(ticker, "revenuePerShare", 0, str(year))
        netIncomePerShare = dt.dataGet(ticker, "netIncomePerShare", 0, str(year))
        operatingCashFlowPerShare = dt.dataGet(ticker, "operatingCashFlowPerShare", 0, str(year))
        freeCashFlowPerShare = dt.dataGet(ticker, "freeCashFlowPerShare", 0, str(year))
        cashPerShare = dt.dataGet(ticker, "cashPerShare", 0, str(year))
        bookValuePerShare = dt.dataGet(ticker, "bookValuePerShare", 0, str(year))
        tangibleBookValuePerShare = dt.dataGet(ticker, "tangibleBookValuePerShare", 0, str(year))
        shareholdersEquityPerShare = dt.dataGet(ticker, "shareholdersEquityPerShare", 0, str(year))
        interestDebtPerShare = dt.dataGet(ticker, "interestDebtPerShare", 0, str(year))
        marketCap = dt.dataGet(ticker, "marketCap", 0, str(year))
        enterpriseValue = dt.dataGet(ticker, "enterpriseValue", 0, str(year))
        try: peRatio = round(float(dt.dataGet(ticker, "peRatio", 0, str(year))), 2)
        except: peRatio = dt.dataGet(ticker, "peRatio", 0, str(year))
        priceToSalesRatio = dt.dataGet(ticker, "priceToSalesRatio", 0, str(year))
        pocfratio = dt.dataGet(ticker, "pocfratio", 0, str(year))
        pfcfRatio = dt.dataGet(ticker, "pfcfRatio", 0, str(year))
        pbRatio = dt.dataGet(ticker, "pbRatio", 0, str(year))
        ptbRatio = dt.dataGet(ticker, "ptbRatio", 0, str(year))
        evToSales = dt.dataGet(ticker, "evToSales", 0, str(year))
        enterpriseValueOverEBITDA = dt.dataGet(ticker, "enterpriseValueOverEBITDA", 0, str(year))
        evToOperatingCashFlow = dt.dataGet(ticker, "evToOperatingCashFlow", 0, str(year))
        evToFreeCashFlow = dt.dataGet(ticker, "evToFreeCashFlow", 0, str(year))
        earningsYield = dt.dataGet(ticker, "earningsYield", 0, str(year))
        freeCashFlowYield = dt.dataGet(ticker, "freeCashFlowYield", 0, str(year))
        debtToEquity = dt.dataGet(ticker, "debtToEquity", 0, str(year))
        debtToAssets = dt.dataGet(ticker, "debtToAssets", 0, str(year))
        netDebtToEBITDA = dt.dataGet(ticker, "netDebtToEBITDA", 0, str(year))
        currentRatio = dt.dataGet(ticker, "currentRatio", 0, str(year))
        interestCoverage = dt.dataGet(ticker, "interestCoverage", 0, str(year))
        incomeQuality = dt.dataGet(ticker, "incomeQuality", 0, str(year))
        dividendYield = dt.dataGet(ticker, "dividendYield", 0, str(year))
        payoutRatio = dt.dataGet(ticker, "payoutRatio", 0, str(year))
        salesGeneralAndAdministrativeToRevenue = dt.dataGet(ticker, "salesGeneralAndAdministrativeToRevenue", 0, str(year))
        researchAndDdevelopementToRevenue = dt.dataGet(ticker, "researchAndDdevelopementToRevenue", 0, str(year))
        intangiblesToTotalAssets = dt.dataGet(ticker, "intangiblesToTotalAssets", 0, str(year))
        capexToOperatingCashFlow = dt.dataGet(ticker, "capexToOperatingCashFlow", 0, str(year))
        capexToRevenue = dt.dataGet(ticker, "capexToRevenue", 0, str(year))
        capexToDepreciation = dt.dataGet(ticker, "capexToDepreciation", 0, str(year))
        stockBasedCompensationToRevenue = dt.dataGet(ticker, "stockBasedCompensationToRevenue", 0, str(year))
        grahamNumber = dt.dataGet(ticker, "grahamNumber", 0, str(year))
        roic = dt.dataGet(ticker, "roic", 0, str(year))
        returnOnTangibleAssets = dt.dataGet(ticker, "returnOnTangibleAssets", 0, str(year))
        grahamNetNet = dt.dataGet(ticker, "grahamNetNet", 0, str(year))
        workingCapital = dt.dataGet(ticker, "workingCapital", 0, str(year))
        tangibleAssetValue = dt.dataGet(ticker, "tangibleAssetValue", 0, str(year))
        netCurrentAssetValue = dt.dataGet(ticker, "netCurrentAssetValue", 0, str(year))
        investedCapital = dt.dataGet(ticker, "investedCapital", 0, str(year))
        averageReceivables = dt.dataGet(ticker, "averageReceivables", 0, str(year))
        averagePayables = dt.dataGet(ticker, "averagePayables", 0, str(year))
        averageInventory = dt.dataGet(ticker, "averageInventory", 0, str(year))
        daysSalesOutstanding = dt.dataGet(ticker, "daysSalesOutstanding", 0, str(year))
        daysPayablesOutstanding = dt.dataGet(ticker, "daysPayablesOutstanding", 0, str(year))
        daysOfInventoryOnHand = dt.dataGet(ticker, "daysOfInventoryOnHand", 0, str(year))
        receivablesTurnover = dt.dataGet(ticker, "receivablesTurnover", 0, str(year))
        payablesTurnover = dt.dataGet(ticker, "payablesTurnover", 0, str(year))
        inventoryTurnover = dt.dataGet(ticker, "inventoryTurnover", 0, str(year))
        capexPerShare = dt.dataGet(ticker, "capexPerShare", 0, str(year))
        #Financial Ratios
        quickRatio = dt.dataGet(ticker, "quickRatio", 0, str(year))
        cashRatio = dt.dataGet(ticker, "cashRatio", 0, str(year))
        daysOfSalesOutstanding = dt.dataGet(ticker, "daysOfSalesOutstanding", 0, str(year))
        daysOfInventoryOutstanding = dt.dataGet(ticker, "daysOfInventoryOutstanding", 0, str(year))
        operatingCycle = dt.dataGet(ticker, "operatingCycle", 0, str(year))
        daysOfPayablesOutstanding = dt.dataGet(ticker, "daysOfPayablesOutstanding", 0, str(year))
        cashConversionCycle = dt.dataGet(ticker, "cashConversionCycle", 0, str(year))
        grossProfitMargin = dt.dataGet(ticker, "grossProfitMargin", 0, str(year))
        operatingProfitMargin = dt.dataGet(ticker, "operatingProfitMargin", 0, str(year))
        pretaxProfitMargin = dt.dataGet(ticker, "pretaxProfitMargin", 0, str(year))
        netProfitMargin = dt.dataGet(ticker, "netProfitMargin", 0, str(year))
        effectiveTaxRate = dt.dataGet(ticker, "effectiveTaxRate", 0, str(year))
        returnOnAssets = dt.dataGet(ticker, "returnOnAssets", 0, str(year))
        returnOnCapitalEmployed = dt.dataGet(ticker, "returnOnCapitalEmployed", 0, str(year))
        netIncomePerEBT = dt.dataGet(ticker, "netIncomePerEBT", 0, str(year))
        ebtPerEbit = dt.dataGet(ticker, "ebtPerEbit", 0, str(year))
        ebitPerRevenue = dt.dataGet(ticker, "ebitPerRevenue", 0, str(year))
        debtRatio = dt.dataGet(ticker, "debtRatio", 0, str(year))
        debtEquityRatio = dt.dataGet(ticker, "debtEquityRatio", 0, str(year))
        longTermDebtToCapitalization = dt.dataGet(ticker, "longTermDebtToCapitalization", 0, str(year))
        totalDebtToCapitalization = dt.dataGet(ticker, "totalDebtToCapitalization", 0, str(year))
        interestCoverage = dt.dataGet(ticker, "interestCoverage", 0, str(year))
        cashFlowToDebtRatio = dt.dataGet(ticker, "cashFlowToDebtRatio", 0, str(year))
        companyEquityMultiplier = dt.dataGet(ticker, "companyEquityMultiplier", 0, str(year))
        fixedAssetTurnover = dt.dataGet(ticker, "fixedAssetTurnover", 0, str(year))
        assetTurnover = dt.dataGet(ticker, "assetTurnover", 0, str(year))
        operatingCashFlowSalesRatio = dt.dataGet(ticker, "operatingCashFlowSalesRatio", 0, str(year))
        freeCashFlowOperatingCashFlowRatio = dt.dataGet(ticker, "freeCashFlowOperatingCashFlowRatio", 0, str(year))
        cashFlowCoverageRatios = dt.dataGet(ticker, "cashFlowCoverageRatios", 0, str(year))
        shortTermCoverageRatios = dt.dataGet(ticker, "shortTermCoverageRatios", 0, str(year))
        capitalExpenditureCoverageRatio = dt.dataGet(ticker, "capitalExpenditureCoverageRatio", 0, str(year))
        dividendPaidAndCapexCoverageRatio = dt.dataGet(ticker, "dividendPaidAndCapexCoverageRatio", 0, str(year))
        priceEarningsToGrowthRatio = dt.dataGet(ticker, "priceEarningsToGrowthRatio", 0, str(year))
        enterpriseValueMultiple = dt.dataGet(ticker, "enterpriseValueMultiple", 0, str(year))
        priceFairValue = dt.dataGet(ticker, "priceFairValue", 0, str(year))
        #Financial Statement Growth
        revenueGrowth = dt.dataGet(ticker, "revenueGrowth", 0, str(year))
        grossProfitGrowth = dt.dataGet(ticker, "grossProfitGrowth", 0, str(year))
        ebitgrowth = dt.dataGet(ticker, "ebitgrowth", 0, str(year))
        operatingIncomeGrowth = dt.dataGet(ticker, "operatingIncomeGrowth", 0, str(year))
        netIncomeGrowth = dt.dataGet(ticker, "netIncomeGrowth", 0, str(year))
        epsgrowth = dt.dataGet(ticker, "epsgrowth", 0, str(year))
        epsdilutedGrowth = dt.dataGet(ticker, "epsdilutedGrowth", 0, str(year))
        weightedAverageSharesGrowth = dt.dataGet(ticker, "weightedAverageSharesGrowth", 0, str(year))
        weightedAverageSharesDilutedGrowth = dt.dataGet(ticker, "weightedAverageSharesDilutedGrowth", 0, str(year))
        dividendsperShareGrowth = dt.dataGet(ticker, "dividendsperShareGrowth", 0, str(year))
        operatingCashFlowGrowth = dt.dataGet(ticker, "operatingCashFlowGrowth", 0, str(year))
        freeCashFlowGrowth = dt.dataGet(ticker, "freeCashFlowGrowth", 0, str(year))
        tenYRevenueGrowthPerShare = dt.dataGet(ticker, "tenYRevenueGrowthPerShare", 0, str(year))
        fiveYRevenueGrowthPerShare = dt.dataGet(ticker, "fiveYRevenueGrowthPerShare", 0, str(year))
        threeYRevenueGrowthPerShare = dt.dataGet(ticker, "threeYRevenueGrowthPerShare", 0, str(year))
        tenYOperatingCFGrowthPerShare = dt.dataGet(ticker, "tenYOperatingCFGrowthPerShare", 0, str(year))
        fiveYOperatingCFGrowthPerShare = dt.dataGet(ticker, "fiveYOperatingCFGrowthPerShare", 0, str(year))
        threeYOperatingCFGrowthPerShare = dt.dataGet(ticker, "threeYOperatingCFGrowthPerShare", 0, str(year))
        tenYNetIncomeGrowthPerShare = dt.dataGet(ticker, "tenYNetIncomeGrowthPerShare", 0, str(year))
        fiveYNetIncomeGrowthPerShare = dt.dataGet(ticker, "fiveYNetIncomeGrowthPerShare", 0, str(year))
        threeYNetIncomeGrowthPerShare = dt.dataGet(ticker, "threeYNetIncomeGrowthPerShare", 0, str(year))
        tenYShareholdersEquityGrowthPerShare = dt.dataGet(ticker, "tenYShareholdersEquityGrowthPerShare", 0, str(year))
        fiveYShareholdersEquityGrowthPerShare = dt.dataGet(ticker, "fiveYShareholdersEquityGrowthPerShare", 0, str(year))
        threeYShareholdersEquityGrowthPerShare = dt.dataGet(ticker, "threeYShareholdersEquityGrowthPerShare", 0, str(year))
        tenYDividendperShareGrowthPerShare = dt.dataGet(ticker, "tenYDividendperShareGrowthPerShare", 0, str(year))
        fiveYDividendperShareGrowthPerShare = dt.dataGet(ticker, "fiveYDividendperShareGrowthPerShare", 0, str(year))
        threeYDividendperShareGrowthPerShare = dt.dataGet(ticker, "threeYDividendperShareGrowthPerShare", 0, str(year))
        receivablesGrowth = dt.dataGet(ticker, "receivablesGrowth", 0, str(year))
        inventoryGrowth = dt.dataGet(ticker, "inventoryGrowth", 0, str(year))
        assetGrowth = dt.dataGet(ticker, "assetGrowth", 0, str(year))
        bookValueperShareGrowth = dt.dataGet(ticker, "bookValueperShareGrowth", 0, str(year))
        debtGrowth = dt.dataGet(ticker, "debtGrowth", 0, str(year))
        rdexpenseGrowth = dt.dataGet(ticker, "rdexpenseGrowth", 0, str(year))
        sgaexpensesGrowth = dt.dataGet(ticker, "sgaexpensesGrowth", 0, str(year))
        #Discounted Cash Flow
        date = dt.dataGet(ticker, "date", 0, str(year))
        stockPrice = dt.dataGet(ticker, "Stock Price", 0, str(year))
        DCF = dt.dataGet(ticker, "DCF", 0, str(year))
    
        Financial(
            #Symbol Data
            symbol = symbol,
            year = year,
            verification = f'{ticker}, {year}',
            fillingDate = fillingDate,
            #Income Statement
            revenue = revenue,
            costOfRevenue = costOfRevenue,
            grossProfit = grossProfit,
            researchAndDevelopmentExpenses = researchAndDevelopmentExpenses,
            generalAndAdministrativeExpenses = generalAndAdministrativeExpenses,
            sellingAndMarketingExpenses = sellingAndMarketingExpenses,
            sellingGeneralAndAdministrativeExpenses = sellingGeneralAndAdministrativeExpenses,
            otherExpenses = otherExpenses,
            operatingExpenses = operatingExpenses,
            costAndExpenses = costAndExpenses,
            interestIncome = interestIncome,
            interestExpense = interestExpense,
            depreciationAndAmortization = depreciationAndAmortization,
            ebitda = ebitda,
            ebitdaratio = ebitdaratio,
            operatingIncome = operatingIncome,
            totalOtherIncomeExpensesNet = totalOtherIncomeExpensesNet,
            incomeBeforeTax = incomeBeforeTax,
            incomeTaxExpense = incomeTaxExpense,
            netIncome = netIncome,
            eps = eps,
            epsdiluted = epsdiluted,
            weightedAverageShsOut = weightedAverageShsOut,
            weightedAverageShsOutDil = weightedAverageShsOutDil,
            #Balance Sheet
            cashAndCashEquivalents = cashAndCashEquivalents,
            shortTermInvestments = shortTermInvestments,
            cashAndShortTermInvestments = cashAndShortTermInvestments,
            netReceivables = netReceivables,
            inventory = inventory,
            otherCurrentAssets = otherCurrentAssets,
            totalCurrentAssets = totalCurrentAssets,
            propertyPlantEquipmentNet = propertyPlantEquipmentNet,
            goodwill = goodwill,
            intangibleAssets = intangibleAssets,
            goodwillAndIntangibleAssets = goodwillAndIntangibleAssets,
            longTermInvestments = longTermInvestments,
            taxAssets = taxAssets,
            otherNonCurrentAssets = otherNonCurrentAssets,
            totalNonCurrentAssets = totalNonCurrentAssets,
            otherAssets = otherAssets,
            totalAssets = totalAssets,
            accountPayables = accountPayables,
            shortTermDebt = shortTermDebt,
            taxPayables = taxPayables,
            deferredRevenue = deferredRevenue,
            otherCurrentLiabilities = otherCurrentLiabilities,
            totalCurrentLiabilities = totalCurrentLiabilities,
            longTermDebt = longTermDebt,
            deferredRevenueNonCurrent = deferredRevenueNonCurrent,
            deferredTaxLiabilitiesNonCurrent = deferredTaxLiabilitiesNonCurrent,
            otherNonCurrentLiabilities = otherNonCurrentLiabilities,
            totalNonCurrentLiabilities = totalNonCurrentLiabilities,
            otherLiabilities = otherLiabilities,
            capitalLeaseObligations = capitalLeaseObligations,
            totalLiabilities = totalLiabilities,
            preferredStock = preferredStock,
            commonStock = commonStock,
            retainedEarnings = retainedEarnings,
            accumulatedOtherComprehensiveIncomeLoss = accumulatedOtherComprehensiveIncomeLoss,
            othertotalStockholdersEquity = othertotalStockholdersEquity,
            totalStockholdersEquity = totalStockholdersEquity,
            totalLiabilitiesAndStockholdersEquity = totalLiabilitiesAndStockholdersEquity,
            minorityInterest = minorityInterest,
            totalEquity = totalEquity,
            totalLiabilitiesAndTotalEquity = totalLiabilitiesAndTotalEquity,
            totalInvestments = totalInvestments,
            totalDebt = totalDebt,
            netDebt = netDebt,
            #Cash Flow
            deferredIncomeTax = deferredIncomeTax,
            stockBasedCompensation = stockBasedCompensation,
            changeInWorkingCapital = changeInWorkingCapital,
            accountsReceivables = accountsReceivables,
            accountsPayables = accountsPayables,
            otherWorkingCapital = otherWorkingCapital,
            otherNonCashItems = otherNonCashItems,
            netCashProvidedByOperatingActivities = netCashProvidedByOperatingActivities,
            investmentsInPropertyPlantAndEquipment = investmentsInPropertyPlantAndEquipment,
            acquisitionsNet = acquisitionsNet,
            purchasesOfInvestments = purchasesOfInvestments,
            salesMaturitiesOfInvestments = salesMaturitiesOfInvestments,
            otherInvestingActivites = otherInvestingActivites,
            netCashUsedForInvestingActivites = netCashUsedForInvestingActivites,
            debtRepayment = debtRepayment,
            commonStockIssued = commonStockIssued,
            commonStockRepurchased = commonStockRepurchased,
            dividendsPaid = dividendsPaid,
            otherFinancingActivites = otherFinancingActivites,
            netCashUsedProvidedByFinancingActivities = netCashUsedProvidedByFinancingActivities,
            effectOfForexChangesOnCash = effectOfForexChangesOnCash,
            netChangeInCash = netChangeInCash,
            cashAtEndOfPeriod = cashAtEndOfPeriod,
            cashAtBeginningOfPeriod = cashAtBeginningOfPeriod,
            operatingCashFlow = operatingCashFlow,
            capitalExpenditure = capitalExpenditure,
            freeCashFlow = freeCashFlow,
            #Key Metrics
            revenuePerShare = revenuePerShare,
            netIncomePerShare = netIncomePerShare,
            operatingCashFlowPerShare = operatingCashFlowPerShare,
            freeCashFlowPerShare = freeCashFlowPerShare,
            cashPerShare = cashPerShare,
            bookValuePerShare = bookValuePerShare,
            tangibleBookValuePerShare = tangibleBookValuePerShare,
            shareholdersEquityPerShare = shareholdersEquityPerShare,
            interestDebtPerShare = interestDebtPerShare,
            marketCap = marketCap,
            enterpriseValue = enterpriseValue,
            peRatio = peRatio,
            priceToSalesRatio = priceToSalesRatio,
            pocfratio = pocfratio,
            pfcfRatio = pfcfRatio,
            pbRatio = pbRatio,
            evToSales = evToSales,
            enterpriseValueOverEBITDA = enterpriseValueOverEBITDA,
            evToOperatingCashFlow = evToOperatingCashFlow,
            evToFreeCashFlow = evToFreeCashFlow,
            earningsYield = earningsYield,
            freeCashFlowYield = freeCashFlowYield,
            debtToEquity = debtToEquity,
            debtToAssets = debtToAssets,
            netDebtToEBITDA = netDebtToEBITDA,
            currentRatio = currentRatio,
            interestCoverage = interestCoverage,
            incomeQuality = incomeQuality,
            dividendYield = dividendYield,
            payoutRatio = payoutRatio,
            salesGeneralAndAdministrativeToRevenue = salesGeneralAndAdministrativeToRevenue,
            researchAndDdevelopementToRevenue = researchAndDdevelopementToRevenue,
            intangiblesToTotalAssets = intangiblesToTotalAssets,
            capexToOperatingCashFlow = capexToOperatingCashFlow,
            capexToRevenue = capexToRevenue,
            capexToDepreciation = capexToDepreciation,
            stockBasedCompensationToRevenue = stockBasedCompensationToRevenue,
            grahamNumber = grahamNumber,
            roic = roic,
            returnOnTangibleAssets = returnOnTangibleAssets,
            grahamNetNet = grahamNetNet,
            workingCapital = workingCapital,
            tangibleAssetValue = tangibleAssetValue,
            netCurrentAssetValue = netCurrentAssetValue,
            investedCapital = investedCapital,
            averageReceivables = averageReceivables,
            averagePayables = averagePayables,
            averageInventory = averageInventory,
            daysSalesOutstanding = daysSalesOutstanding,
            daysPayablesOutstanding = daysPayablesOutstanding,
            daysOfInventoryOnHand = daysOfInventoryOnHand,
            receivablesTurnover = receivablesTurnover,
            payablesTurnover = payablesTurnover,
            inventoryTurnover = inventoryTurnover,
            capexPerShare = capexPerShare,
            #Financial Ratios
            quickRatio = quickRatio,
            cashRatio = cashRatio,
            daysOfSalesOutstanding = daysOfSalesOutstanding,
            daysOfInventoryOutstanding = daysOfInventoryOutstanding,
            operatingCycle = operatingCycle,
            daysOfPayablesOutstanding = daysOfPayablesOutstanding,
            cashConversionCycle = cashConversionCycle,
            grossProfitMargin = grossProfitMargin,
            operatingProfitMargin = operatingProfitMargin,
            pretaxProfitMargin = pretaxProfitMargin,
            netProfitMargin = netProfitMargin,
            effectiveTaxRate = effectiveTaxRate,
            returnOnCapitalEmployed = returnOnCapitalEmployed,
            netIncomePerEBT = netIncomePerEBT,
            ebtPerEbit = ebtPerEbit,
            ebitPerRevenue = ebitPerRevenue,
            debtRatio = debtRatio,
            debtEquityRatio = debtEquityRatio,
            longTermDebtToCapitalization = longTermDebtToCapitalization,
            totalDebtToCapitalization = totalDebtToCapitalization,
            cashFlowToDebtRatio = cashFlowToDebtRatio,
            companyEquityMultiplier = companyEquityMultiplier,
            fixedAssetTurnover = fixedAssetTurnover,
            assetTurnover = assetTurnover,
            operatingCashFlowSalesRatio = operatingCashFlowSalesRatio,
            freeCashFlowOperatingCashFlowRatio = freeCashFlowOperatingCashFlowRatio,
            cashFlowCoverageRatios = cashFlowCoverageRatios,
            shortTermCoverageRatios = shortTermCoverageRatios,
            capitalExpenditureCoverageRatio = capitalExpenditureCoverageRatio,
            dividendPaidAndCapexCoverageRatio = dividendPaidAndCapexCoverageRatio,
            enterpriseValueMultiple = enterpriseValueMultiple,
            priceFairValue = priceFairValue,
            #Financial Statement Growth
            revenueGrowth = revenueGrowth,
            grossProfitGrowth = grossProfitGrowth,
            ebitgrowth = ebitgrowth,
            operatingIncomeGrowth = operatingIncomeGrowth,
            netIncomeGrowth = netIncomeGrowth,
            epsgrowth = epsgrowth,
            epsdilutedGrowth = epsdilutedGrowth,
            weightedAverageSharesGrowth = weightedAverageSharesGrowth,
            weightedAverageSharesDilutedGrowth = weightedAverageSharesDilutedGrowth,
            dividendsperShareGrowth = dividendsperShareGrowth,
            operatingCashFlowGrowth = operatingCashFlowGrowth,
            freeCashFlowGrowth = freeCashFlowGrowth,
            tenYRevenueGrowthPerShare = tenYRevenueGrowthPerShare,
            fiveYRevenueGrowthPerShare = fiveYRevenueGrowthPerShare,
            threeYRevenueGrowthPerShare = threeYRevenueGrowthPerShare,
            tenYOperatingCFGrowthPerShare = tenYOperatingCFGrowthPerShare,
            fiveYOperatingCFGrowthPerShare = fiveYOperatingCFGrowthPerShare,
            threeYOperatingCFGrowthPerShare = threeYOperatingCFGrowthPerShare,
            tenYNetIncomeGrowthPerShare = tenYNetIncomeGrowthPerShare,
            fiveYNetIncomeGrowthPerShare = fiveYNetIncomeGrowthPerShare,
            threeYNetIncomeGrowthPerShare = threeYNetIncomeGrowthPerShare,
            tenYShareholdersEquityGrowthPerShare = tenYShareholdersEquityGrowthPerShare,
            fiveYShareholdersEquityGrowthPerShare = fiveYShareholdersEquityGrowthPerShare,
            threeYShareholdersEquityGrowthPerShare = threeYShareholdersEquityGrowthPerShare,
            tenYDividendperShareGrowthPerShare = tenYDividendperShareGrowthPerShare,
            fiveYDividendperShareGrowthPerShare = fiveYDividendperShareGrowthPerShare,
            threeYDividendperShareGrowthPerShare = threeYDividendperShareGrowthPerShare,
            receivablesGrowth = receivablesGrowth,
            inventoryGrowth = inventoryGrowth,
            assetGrowth = assetGrowth,
            bookValueperShareGrowth = bookValueperShareGrowth,
            debtGrowth = debtGrowth,
            rdexpenseGrowth = rdexpenseGrowth,
            sgaexpensesGrowth = sgaexpensesGrowth,
            #Discounted Cash Flow
            date = date,
            stockPrice = stockPrice,
            DCF = DCF, 
        ).save()
        
        ShortFinancial(
            symbol = symbol,
            year = year,
            verification = f'{ticker}, {year}',
            revenue = revenue,
            eps = eps,
            marketCap = marketCap,
            enterpriseValue = enterpriseValue,
            peRatio = peRatio,
            priceToSalesRatio = priceToSalesRatio,
            pfcfRatio = pfcfRatio,
            pbRatio = pbRatio,
            debtToEquity = debtToEquity,
            debtToAssets = debtToAssets,
            netDebtToEBITDA = netDebtToEBITDA,
            currentRatio = currentRatio,
            dividendYield = dividendYield,
            payoutRatio = payoutRatio,
            roic = roic,
            quickRatio = quickRatio,
            cashRatio = cashRatio,
            grossProfitMargin = grossProfitMargin,
            operatingProfitMargin = operatingProfitMargin,
            pretaxProfitMargin = pretaxProfitMargin,
            netProfitMargin = netProfitMargin,
            debtRatio = debtRatio,
            assetTurnover = assetTurnover,
            revenueGrowth = revenueGrowth,
            debtGrowth = debtGrowth,
            DCF = DCF,
        ).save()
        print(f"'{ticker}' Financial Model for {year} saved.")
        
    #Info Model    
    Info(
        symbol=symbol,
        ticker=ticker,
        city=city, 
        state=state, 
        country=country, 
        address=address, 
        name=name,
        summary=summary,
        employees=employees,
        sector=sector,
        industry=industry,
        exchange=exchange,
        quoteType=quoteType,
        currency=currency,
        marketCap=marketCap,
        phone=phone,
        website=website,
        logo=logo,
        period=period,
        cik=cik,
        link=link,
        finalLink=finalLink,
    ).save()
    print(f"'{ticker}' Info Model saved.")




class Command(BaseCommand):
    
    def add_arguments(self, parser):
        pass
    
    def handle(sef, *args, **options):
        skip = False
        single = True
        if (single == False):
            tickers = dt.tickers_sp500
            for ticker in tickers:
                DataTransfer(ticker)
        else:
            ticker = "ADBE"
            DataTransfer(ticker)
            
            
    
        
        
            

    

