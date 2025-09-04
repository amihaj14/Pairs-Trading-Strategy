import yfinance as yf
import pandas as pd

stock1 = yf.download("KO", start="2015-01-01", end="2023-12-31", auto_adjust = False) #Coca-Cola Data
stock2 = yf.download("PEP", start="2015-01-01", end="2023-12-31", auto_adjust = False) #Pepsi Data

prices = pd.concat([stock1['Adj Close'], stock2['Adj Close']], axis=1)
prices.columns = ['KO', 'PEP']
prices.dropna(inplace=True)
