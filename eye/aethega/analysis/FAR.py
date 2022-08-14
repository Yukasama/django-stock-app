
#Dependencies
import sys
from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(BASE_DIR)
from data.datahandler import *
import matplotlib.pyplot as plt
from matplotlib import style as style
import numpy as np
import pandas as pd
import datetime as dt
import time
import math


#-------------------------------------------------------------------------------------------------------------------


def sectorAverage(tickerAsArray, value, attribute, progress=False):
    
    #Function Globals
    averageValue = []
    sectorCounter, industryCounter, category, count, minus = 0, 0, 0, 0, 0
    
    if(progress == True):
        print("Determine Category..")

    #Select Category automatically
    for t in tickerAsArray:
        sectorValue = data.dataGet(t, "sector", "info")
        industryValue = data.dataGet(t, "industry", "info")
        if (sectorValue == attribute): sectorCounter += 1
        elif (industryValue == attribute): industryCounter += 1
        
    if (sectorCounter != 0): category = "sector"
    elif (industryCounter != 0): category = "industry"
    else: 
        print("No sector/industry found.")
        exit()
        
    if(progress == True):
        print(f"Success! Category: {category.capitalize()}")
        print(f"Starting CSV Extracting..")
        time.sleep(1)
        
    #Create Average Array
    for t in tickerAsArray: 
        categoryValue = data.dataGet(t, category, "info")
        try: request = float(data.dataGet(t, value))
        except:
            continue
        if (categoryValue == attribute):            
            if not(math.isnan(request)):
                if(progress == True):
                    print(f"{t}: {request}")
                averageValue.append(request)
                count += 1
    
    #Calculate Average
    try:
        average = sum(averageValue) / (len(averageValue))
        return average, count
    except: 
        print("Value doesn't exist.")
        return 0
    

#-------------------------------------------------------------------------------------------------------------------


def valueRegister():
            
    #Income Statement
    eps = { lower: 1, higher: 5, path: "higher"}
    peRatio = { lower: -10, best: 15, higher: 50, path: "best"}
    revenue = {path: "relative"}

    #Financial Ratios
    # grossMargin = { lower: 0.05, higher: 0.5, path: higher }
    # operatingMargin = { lower: -0.05, higher: 0.4, path: higher}
    # profitMargin = { lower: -0.1, higher: 0.3, path: higher}
    
    print(eps[lower])
    

#-------------------------------------------------------------------------------------------------------------------


def FAR(tickerAsArray):
    
    #Settings
    WeightedAveraging = True
    SectorBalancing = False
    StandardDeviation = True
    Timefluence = True
    AllowForecast = False
    
    eps = dataGet(tickerAsArray, "eps", 0, "ALL")
    revenue = dataGet(tickerAsArray, "revenue", 0, "ALL")
    grossMargin = dataGet(tickerAsArray, "grossProfitMargin", 0, "ALL")
    operatingMargin = dataGet(tickerAsArray, "operatingProfitMargin", 0, "ALL")
    profitMargin = dataGet(tickerAsArray, "netProfitMargin", 0, "ALL")
    print(grossMargin, operatingMargin, profitMargin)
    plt.style.use(['dark_background'])
    
    array = [grossMargin, operatingMargin, profitMargin]
    for i in array:
        plt.plot(i)
    plt.show()


#-------------------------------------------------------------------------------------------------------------------

        
        
FAR("AAPL")