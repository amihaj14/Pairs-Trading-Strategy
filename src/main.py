import matplotlib.pyplot as plt 
import DataLoader
import Backtest
import Strategy
import pandas as pd

# pairs =[
#      ("KO", "PEP"),
#      ("MSFT", "AAPL"),
#      ("JPM", "BAC")
# ]

# prices = DataLoader.load_prices(pairs, start="2015-01-01")

# results = []

# for stock1, stock2 in pairs:
#print(f"\n----- Testing Pair: {stock1}-{stock2} -----")

alpha, beta, residuals = Strategy.lin_reg(DataLoader.prices["KO"], DataLoader.prices["PEP"])

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

    #Storing results
    # metrics["Pair"] = f"{stock1}-{stock2}"
    # results.append(metrics)

else:
    print("No cointegration found. Strategy not applicable.")

# resultsDF = pd.DataFrame(results)
# print(f"\n----- Strategy Comparison -----")
# print(resultsDF)

