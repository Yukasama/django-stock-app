
import datahandler as data, technicals as tech, fundamentals as fund
import pandas as pd
import matplotlib.pyplot as plt

# Data Functions
# data.fundamentalData(data.tickers_sp500)
# data.dataPush(data.tickers_sp500, pushRate=0, skipMode=False, single="history")

tar = tech.TAR(data.tickers_sp500, progress=True)
print(tar)

