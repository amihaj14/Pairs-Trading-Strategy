import yfinance as yf
import pandas as pd

# def load_prices(tickers, start="2015-01-01", end=None):
#     data = yf.download(tickers, start=start, end=end, group_by="ticker")

#     print("Columns type:", type(data.columns))
#     if isinstance(data.columns, pd.MultiIndex):
#         print("MultiIndex levels:", data.columns.names)
#         print("Top 5 column tuples:")
#         for col in data.columns[:5]:
#             print(col)
#     else:
#         print("Columns:", data.columns.tolist())

#     # Now try to extract prices
#     if isinstance(data.columns, pd.MultiIndex):
#         print("\nLevel 0 (price types):", data.columns.get_level_values(0).unique().tolist())
#         print("Level 1 (tickers):", data.columns.get_level_values(1).unique().tolist())

#     return data  # ← Return raw data for inspection


stock1 = yf.download("KO", start="2015-01-01", end="2023-12-31", auto_adjust = False) #Coca-Cola Data
stock2 = yf.download("PEP", start="2015-01-01", end="2023-12-31", auto_adjust = False) #Pepsi Data

prices = pd.concat([stock1['Adj Close'], stock2['Adj Close']], axis=1)
prices.columns = ['KO', 'PEP']
prices.dropna(inplace=True)
