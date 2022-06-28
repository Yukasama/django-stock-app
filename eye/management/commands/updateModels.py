from django.core.management.base import BaseCommand
from eye.models import Stock, Info, Financial, ShortFinancial
from eye.stocks import datahandler as dt
import pandas as pd
import datetime
import time
from collections import defaultdict



def DataTransfer(ticker, skip=False):
    
    df = dt.dataGet(ticker, "all")
    dfi = dt.dataGet(ticker, 0, "info")
    if df.empty: print(f'{ticker} Data not pushed yet => Skipped')
    else:
        
        startTime = time.time()

        #Duplicate Handling  
        try:
            Stock.objects.delete(symbol=ticker)
            symbol = Stock.objects.create(symbol=ticker)
        except:
            symbol = Stock.objects.create(symbol=ticker)
            
        for stock in Stock.objects.all():
            if Stock.objects.filter(symbol=stock.symbol).count() > 1:
                stock.delete()
                
        #Info Data
        infoStrings = [i.name for i in Info._meta.get_fields()]
        infodict = {}
        for i in infoStrings:
            if (i == "period" or i == "cik" or i == "link" or i == "finalLink"):
                try: infodict[i] = df.loc[df["Unnamed: 0"] == i]["2021"].tolist()[0]
                except: infodict[i] = "N/A"
            else:
                try: infodict[i] = dfi.loc[dfi["Unnamed: 0"] == i]["0"].tolist()[0]
                except: 
                    infodict[i] = "N/A"
                    print(i + " didnt work.")
        
        #Financial Data
        finStrings = [f.name for f in Financial._meta.get_fields()]
        findict = {}
        for year in range(2015, 2022):
            for f in finStrings:
                if (f == "symbol" or f == "year" or f == "verification" or f == "stockPrice"): continue
                try: findict[f] = df.loc[df["Unnamed: 0"] == f][str(year)].tolist()[0]
                except: 
                    print(f + " didnt work.")
                
            Financial(
                #Symbol Data
                symbol = symbol,
                year = year,
                verification = f'{ticker}, {year}',
                fillingDate = findict["fillingDate"],
                revenue = findict["revenue"],
                costOfRevenue = findict["costOfRevenue"],
                grossProfit = findict["grossProfit"],
                researchAndDevelopmentExpenses = findict["researchAndDevelopmentExpenses"],
                generalAndAdministrativeExpenses = findict["generalAndAdministrativeExpenses"],
                sellingAndMarketingExpenses = findict["sellingAndMarketingExpenses"],
                sellingGeneralAndAdministrativeExpenses = findict["sellingGeneralAndAdministrativeExpenses"],
                otherExpenses = findict["otherExpenses"],
                operatingExpenses = findict["operatingExpenses"],
                costAndExpenses = findict["costAndExpenses"],
                interestIncome = findict["interestIncome"],
                interestExpense = findict["interestExpense"],
                depreciationAndAmortization = findict["depreciationAndAmortization"],
                ebitda = findict["ebitda"],
                ebitdaratio = findict["ebitdaratio"],
                operatingIncome = findict["operatingIncome"],
                totalOtherIncomeExpensesNet = findict["totalOtherIncomeExpensesNet"],
                incomeBeforeTax = findict["incomeBeforeTax"],
                incomeTaxExpense = findict["incomeTaxExpense"],
                netIncome = findict["netIncome"],
                eps = findict["eps"],
                epsdiluted = findict["epsdiluted"],
                weightedAverageShsOut = findict["weightedAverageShsOut"],
                weightedAverageShsOutDil = findict["weightedAverageShsOutDil"],
                cashAndCashEquivalents = findict["cashAndCashEquivalents"],
                shortTermInvestments = findict["shortTermInvestments"],
                cashAndShortTermInvestments = findict["cashAndShortTermInvestments"],
                netReceivables = findict["netReceivables"],
                inventory = findict["inventory"],
                otherCurrentAssets = findict["otherCurrentAssets"],
                totalCurrentAssets = findict["totalCurrentAssets"],
                propertyPlantEquipmentNet = findict["propertyPlantEquipmentNet"],
                goodwill = findict["goodwill"],
                intangibleAssets = findict["intangibleAssets"],
                goodwillAndIntangibleAssets = findict["goodwillAndIntangibleAssets"],
                longTermInvestments = findict["longTermInvestments"],
                taxAssets = findict["taxAssets"],
                otherNonCurrentAssets = findict["otherNonCurrentAssets"],
                totalNonCurrentAssets = findict["totalNonCurrentAssets"],
                otherAssets = findict["otherAssets"],
                totalAssets = findict["totalAssets"],
                accountPayables = findict["accountPayables"],
                shortTermDebt = findict["shortTermDebt"],
                taxPayables = findict["taxPayables"],
                deferredRevenue = findict["deferredRevenue"],
                otherCurrentLiabilities = findict["otherCurrentLiabilities"],
                totalCurrentLiabilities = findict["totalCurrentLiabilities"],
                longTermDebt = findict["longTermDebt"],
                deferredRevenueNonCurrent = findict["deferredRevenueNonCurrent"],
                deferredTaxLiabilitiesNonCurrent = findict["deferredTaxLiabilitiesNonCurrent"],
                otherNonCurrentLiabilities = findict["otherNonCurrentLiabilities"],
                totalNonCurrentLiabilities = findict["totalNonCurrentLiabilities"],
                otherLiabilities = findict["otherLiabilities"],
                capitalLeaseObligations = findict["capitalLeaseObligations"],
                totalLiabilities = findict["totalLiabilities"],
                preferredStock = findict["preferredStock"],
                commonStock = findict["commonStock"],
                retainedEarnings = findict["retainedEarnings"],
                accumulatedOtherComprehensiveIncomeLoss = findict["accumulatedOtherComprehensiveIncomeLoss"],
                othertotalStockholdersEquity = findict["othertotalStockholdersEquity"],
                totalStockholdersEquity = findict["totalStockholdersEquity"],
                totalLiabilitiesAndStockholdersEquity = findict["totalLiabilitiesAndStockholdersEquity"],
                minorityInterest = findict["minorityInterest"],
                totalEquity = findict["totalEquity"],
                totalLiabilitiesAndTotalEquity = findict["totalLiabilitiesAndTotalEquity"],
                totalInvestments = findict["totalInvestments"],
                totalDebt = findict["totalDebt"],
                netDebt = findict["netDebt"],
                deferredIncomeTax = findict["deferredIncomeTax"],
                stockBasedCompensation = findict["stockBasedCompensation"],
                changeInWorkingCapital = findict["changeInWorkingCapital"],
                accountsReceivables = findict["accountsReceivables"],
                accountsPayables = findict["accountsPayables"],
                otherWorkingCapital = findict["otherWorkingCapital"],
                otherNonCashItems = findict["otherNonCashItems"],
                netCashProvidedByOperatingActivities = findict["netCashProvidedByOperatingActivities"],
                investmentsInPropertyPlantAndEquipment = findict["investmentsInPropertyPlantAndEquipment"],
                acquisitionsNet = findict["acquisitionsNet"],
                purchasesOfInvestments = findict["purchasesOfInvestments"],
                salesMaturitiesOfInvestments = findict["salesMaturitiesOfInvestments"],
                otherInvestingActivites = findict["otherInvestingActivites"],
                netCashUsedForInvestingActivites = findict["netCashUsedForInvestingActivites"],
                debtRepayment = findict["debtRepayment"],
                commonStockIssued = findict["commonStockIssued"],
                commonStockRepurchased = findict["commonStockRepurchased"],
                dividendsPaid = findict["dividendsPaid"],
                otherFinancingActivites = findict["otherFinancingActivites"],
                netCashUsedProvidedByFinancingActivities = findict["netCashUsedProvidedByFinancingActivities"],
                effectOfForexChangesOnCash = findict["effectOfForexChangesOnCash"],
                netChangeInCash = findict["netChangeInCash"],
                cashAtEndOfPeriod = findict["cashAtEndOfPeriod"],
                cashAtBeginningOfPeriod = findict["cashAtBeginningOfPeriod"],
                operatingCashFlow = findict["operatingCashFlow"],
                capitalExpenditure = findict["capitalExpenditure"],
                freeCashFlow = findict["freeCashFlow"],
                revenuePerShare = findict["revenuePerShare"],
                netIncomePerShare = findict["netIncomePerShare"],
                operatingCashFlowPerShare = findict["operatingCashFlowPerShare"],
                freeCashFlowPerShare = findict["freeCashFlowPerShare"],
                cashPerShare = findict["cashPerShare"],
                bookValuePerShare = findict["bookValuePerShare"],
                tangibleBookValuePerShare = findict["tangibleBookValuePerShare"],
                shareholdersEquityPerShare = findict["shareholdersEquityPerShare"],
                interestDebtPerShare = findict["interestDebtPerShare"],
                marketCap = findict["marketCap"],
                enterpriseValue = findict["enterpriseValue"],
                peRatio = findict["peRatio"],
                priceToSalesRatio = findict["priceToSalesRatio"],
                pocfratio = findict["pocfratio"],
                pfcfRatio = findict["pfcfRatio"],
                pbRatio = findict["pbRatio"],
                evToSales = findict["evToSales"],
                enterpriseValueOverEBITDA = findict["enterpriseValueOverEBITDA"],
                evToOperatingCashFlow = findict["evToOperatingCashFlow"],
                evToFreeCashFlow = findict["evToFreeCashFlow"],
                earningsYield = findict["earningsYield"],
                freeCashFlowYield = findict["freeCashFlowYield"],
                debtToEquity = findict["debtToEquity"],
                debtToAssets = findict["debtToAssets"],
                netDebtToEBITDA = findict["netDebtToEBITDA"],
                currentRatio = findict["currentRatio"],
                interestCoverage = findict["interestCoverage"],
                incomeQuality = findict["incomeQuality"],
                dividendYield = findict["dividendYield"],
                payoutRatio = findict["payoutRatio"],
                salesGeneralAndAdministrativeToRevenue = findict["salesGeneralAndAdministrativeToRevenue"],
                researchAndDdevelopementToRevenue = findict["researchAndDdevelopementToRevenue"],
                intangiblesToTotalAssets = findict["intangiblesToTotalAssets"],
                capexToOperatingCashFlow = findict["capexToOperatingCashFlow"],
                capexToRevenue = findict["capexToRevenue"],
                capexToDepreciation = findict["capexToDepreciation"],
                stockBasedCompensationToRevenue = findict["stockBasedCompensationToRevenue"],
                grahamNumber = findict["grahamNumber"],
                roic = findict["roic"],
                returnOnTangibleAssets = findict["returnOnTangibleAssets"],
                grahamNetNet = findict["grahamNetNet"],
                workingCapital = findict["workingCapital"],
                tangibleAssetValue = findict["tangibleAssetValue"],
                netCurrentAssetValue = findict["netCurrentAssetValue"],
                investedCapital = findict["investedCapital"],
                averageReceivables = findict["averageReceivables"],
                averagePayables = findict["averagePayables"],
                averageInventory = findict["averageInventory"],
                daysSalesOutstanding = findict["daysSalesOutstanding"],
                daysPayablesOutstanding = findict["daysPayablesOutstanding"],
                daysOfInventoryOnHand = findict["daysOfInventoryOnHand"],
                receivablesTurnover = findict["receivablesTurnover"],
                payablesTurnover = findict["payablesTurnover"],
                inventoryTurnover = findict["inventoryTurnover"],
                capexPerShare = findict["capexPerShare"],
                quickRatio = findict["quickRatio"],
                cashRatio = findict["cashRatio"],
                daysOfSalesOutstanding = findict["daysOfSalesOutstanding"],
                daysOfInventoryOutstanding = findict["daysOfInventoryOutstanding"],
                operatingCycle = findict["operatingCycle"],
                daysOfPayablesOutstanding = findict["daysOfPayablesOutstanding"],
                cashConversionCycle = findict["cashConversionCycle"],
                grossProfitMargin = findict["grossProfitMargin"],
                operatingProfitMargin = findict["operatingProfitMargin"],
                pretaxProfitMargin = findict["pretaxProfitMargin"],
                netProfitMargin = findict["netProfitMargin"],
                effectiveTaxRate = findict["effectiveTaxRate"],
                returnOnAssets = findict["returnOnAssets"],
                returnOnCapitalEmployed = findict["returnOnCapitalEmployed"],
                netIncomePerEBT = findict["netIncomePerEBT"],
                ebtPerEbit = findict["ebtPerEbit"],
                ebitPerRevenue = findict["ebitPerRevenue"],
                debtRatio = findict["debtRatio"],
                debtEquityRatio = findict["debtEquityRatio"],
                longTermDebtToCapitalization = findict["longTermDebtToCapitalization"],
                totalDebtToCapitalization = findict["totalDebtToCapitalization"],
                cashFlowToDebtRatio = findict["cashFlowToDebtRatio"],
                companyEquityMultiplier = findict["companyEquityMultiplier"],
                fixedAssetTurnover = findict["fixedAssetTurnover"],
                assetTurnover = findict["assetTurnover"],
                operatingCashFlowSalesRatio = findict["operatingCashFlowSalesRatio"],
                freeCashFlowOperatingCashFlowRatio = findict["freeCashFlowOperatingCashFlowRatio"],
                cashFlowCoverageRatios = findict["cashFlowCoverageRatios"],
                shortTermCoverageRatios = findict["shortTermCoverageRatios"],
                capitalExpenditureCoverageRatio = findict["capitalExpenditureCoverageRatio"],
                dividendPaidAndCapexCoverageRatio = findict["dividendPaidAndCapexCoverageRatio"],
                priceEarningsToGrowthRatio = findict["priceEarningsToGrowthRatio"],
                enterpriseValueMultiple = findict["enterpriseValueMultiple"],
                priceFairValue = findict["priceFairValue"],
                stockPrice = 0,
                DCF = findict["DCF"],
            ).save()
            
            ShortFinancial(
                symbol = symbol,
                year = year,
                verification = f'{ticker}, {year}',
                revenue = findict["revenue"],
                eps = findict["eps"],
                marketCap = findict["marketCap"],
                enterpriseValue = findict["enterpriseValue"],
                peRatio = findict["peRatio"],
                priceToSalesRatio = findict["priceToSalesRatio"],
                pfcfRatio = findict["pfcfRatio"],
                pbRatio = findict["pbRatio"],
                debtToEquity = findict["debtToEquity"],
                debtToAssets = findict["debtToAssets"],
                netDebtToEBITDA = findict["netDebtToEBITDA"],
                currentRatio = findict["currentRatio"],
                dividendYield = findict["dividendYield"],
                payoutRatio = findict["payoutRatio"],
                roic = findict["roic"],
                quickRatio = findict["quickRatio"],
                cashRatio = findict["cashRatio"],
                grossProfitMargin = findict["grossProfitMargin"],
                operatingProfitMargin = findict["operatingProfitMargin"],
                netProfitMargin = findict["netProfitMargin"],
                debtRatio = findict["debtRatio"],
                assetTurnover = findict["assetTurnover"],
                DCF = findict["DCF"],
            ).save()
            print(f"'{ticker}' Financial Model for {year} saved.")
            
        #Info Model
        Info(
            symbol=symbol,
            ticker=ticker,
            city=infodict["city"], 
            state=infodict["state"], 
            country=infodict["country"], 
            address1=infodict["address1"], 
            longName=infodict["longName"],
            longBusinessSummary=infodict["longBusinessSummary"],
            fullTimeEmployees=infodict["fullTimeEmployees"],
            sector=infodict["sector"],
            industry=infodict["industry"],
            exchange=infodict["exchange"],
            quoteType=infodict["quoteType"],
            currency=infodict["currency"],
            marketCap=infodict["marketCap"],
            recommendationMean = infodict["recommendationMean"],
            targetMeanPrice = infodict["targetMeanPrice"],
            dividendRate = infodict["dividendRate"],
            beta = infodict["beta"],
            shortRatio = infodict["shortRatio"],
            forwardEps = infodict["forwardEps"],
            pegRatio = infodict["pegRatio"],
            phone=infodict["phone"],
            website=infodict["website"],
            logo_url=infodict["logo_url"],
            period=infodict["period"],
            cik=infodict["cik"],
            link=infodict["link"],
            finalLink=infodict["finalLink"],
        ).save()
        print(f"'{ticker}' Info Model saved.")
        
        executionTime = round(time.time() - startTime, 5)
        print(f'Executed in: {executionTime}s')




class Command(BaseCommand):
    
    def add_arguments(self, parser):
        pass
    
    def handle(sef, *args, **options):
        skip = False
        single = False
        if (single == False):
            tickers = dt.tickers_sp500
            for ticker in tickers:
                DataTransfer(ticker, skip=False)
        else:
            ticker = "AAPL"
            DataTransfer(ticker)
            
            
    
        
        
            

    

