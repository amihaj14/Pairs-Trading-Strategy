import matplotlib.pyplot as plt 
import DataLoader
import Backtest
import Strategy
import pandas as pd

#Gets values from Strategy.py file 
alpha, beta, residuals = Strategy.lin_reg(DataLoader.prices["KO"], DataLoader.prices["PEP"])

#Checks if the pair being analyzed is cointegrated
if Strategy.pVal < 0.05:
    zscore = Strategy.z_score(residuals)
    signals = Strategy.generate_signals(zscore)

    #Z-score plot
    plt.figure(figsize=(12,6))
    plt.plot(zscore, label="z-score")
    plt.axhline(1, color="red", linestyle="--", label="Sell threshold")
    plt.axhline(-1, color="green", linestyle="--", label="Buy threshold")
    plt.legend()
    plt.title("Z-score Trading Signals")
    plt.show()

    #Backtesting
    stratReturn, cumulative, metrics = Backtest.backtest(DataLoader.prices[["KO","PEP"]], signals, beta, residuals)

else:
    print("No cointegration found. Strategy not applicable.")

