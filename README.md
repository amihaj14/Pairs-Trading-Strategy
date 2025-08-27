# Pairs-Trading-Strategy

A pairs trading strategy using cointegration and mean-reversion methods in Python.

## Overview
Pairs trading is a strategy where a trader buys one security and shorts another, with a high historical correlation, to profit from the price divergence or convergence. The goal is to assume that the spread between the two highly correlated options will revert to its historical mean. Coca-Cola and pepsi are two highly cointegrated pairs, hence their prices tend to fluctuate similarily, that are expected to revert to their historical mean.

## Methodology
- Engle-Granger test
  - Used to test for cointegration between the two securities, in this case stocks
- Spread regression
  - Unlike traditional regression, it incorporates measures variability like standard deviation into the model
- Z-score thresholds
  - A z-score threshold of ±1 is used in order to indicate buy and sell signals
  - The buy signal occurs once the z-score crosses from above to below the threshold
  - The sell signal occurs once the z-score crosses from below to above the threshold
- Backtesting

## Results

## How To Run
**Run this in powershell**
git clone https://github.com/amihaj14/pairs-trading-strategy.git <br/>
cd pairs-trading-strategy <br/>
pip install -r requirements.txt <br/>
python src/main.py <br/>
