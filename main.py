import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and date range
symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-01"

# Retrieve historical stock price data
data = yf.download(symbol, start=start_date, end=end_date, progress=False)

# Calculate the 20-day moving average
data['MA20'] = data['Close'].rolling(window=20).mean()

# Calculate the standard deviation
data['STD'] = data['Close'].rolling(window=20).std()

# Calculate the upper and lower Bollinger Bands
data['UpperBand'] = data['MA20'] + 2 * data['STD']
data['LowerBand'] = data['MA20'] - 2 * data['STD']

# Generate trading signals for Bollinger Bands strategy
data['Signal'] = 0
data.loc[data['Close'] > data['UpperBand'], 'Signal'] = -1  # Sell signal
data.loc[data['Close'] < data['LowerBand'], 'Signal'] = 1  # Buy signal

# Calculate the daily returns
data['Returns'] = data['Close'].pct_change()

# Calculate the strategy returns for Bollinger Bands strategy
data['StrategyReturns'] = data['Signal'].shift(1) * data['Returns']

# Calculate the cumulative returns for Bollinger Bands strategy
data['CumulativeReturns'] = (1 + data['StrategyReturns']).cumprod()

# Calculate the cumulative returns for buy and hold strategy
data['BuyHoldReturns'] = (1 + data['Returns']).cumprod()

# Plot the stock price and Bollinger Bands with trading signals
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Stock Price')
plt.plot(data['MA20'], label='20-day MA')
plt.plot(data['UpperBand'], label='Upper Bollinger Band')
plt.plot(data['LowerBand'], label='Lower Bollinger Band')
plt.scatter(data[data['Signal'] == 1].index, data['Close'][data['Signal'] == 1], marker='^', color='g', label='Buy')
plt.scatter(data[data['Signal'] == -1].index, data['Close'][data['Signal'] == -1], marker='v', color='r', label='Sell')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'{symbol} Stock Price with Bollinger Bands and Trading Signals (2022)')
plt.legend()

# Create a secondary y-axis for cumulative returns
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Plot cumulative returns for Bollinger Bands strategy
ax1.plot(data['CumulativeReturns'], label='Bollinger Bands Strategy', color='b')
ax1.set_ylabel('Cumulative Returns')
ax1.set_xlabel('Date')

# Plot cumulative returns for buy and hold strategy
ax2.plot(data['BuyHoldReturns'], label='Buy and Hold Strategy', color='g')
ax2.set_ylabel('Cumulative Returns')

# Set titles and legends
ax1.set_title(f'{symbol} Cumulative Returns: Bollinger Bands vs. Buy and Hold (2022)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()
