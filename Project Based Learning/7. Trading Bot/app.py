import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch Data
ticker = 'NVDA'
data = yf.download(ticker, period='1y', interval='1h')

# Check if data is fetched
if data.empty:
    print("No data fetched. Please check your internet connection and ticker symbol.")
    exit()

# Calculate Moving Averages with smaller windows
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA10'] = data['Close'].rolling(window=10).mean()

# Drop initial NaN values
data.dropna(inplace=True)

# Check if data is empty after dropping NaNs
if data.empty:
    print("Data is empty after dropping NaN values. Try fetching more data or adjusting the rolling window sizes.")
    exit()

# Generate Signals
data['Signal'] = np.where(data['MA5'] > data['MA10'], 1, 0)

# Generate Trading Orders
data['Position'] = data['Signal'].diff()

# Backtesting
initial_capital = 10000.0
positions = pd.DataFrame(index=data.index).fillna(0.0)
positions[ticker] = data['Signal']

portfolio = pd.DataFrame(index=data.index)
portfolio['holdings'] = positions[ticker] * data['Adj Close']
portfolio['cash'] = initial_capital - (positions[ticker].diff() * data['Adj Close']).cumsum().fillna(0)
portfolio['total'] = portfolio['cash'] + portfolio['holdings']
portfolio['returns'] = portfolio['total'].pct_change().fillna(0)
portfolio['cumulative_returns'] = (1 + portfolio['returns']).cumprod() - 1

# Check if portfolio is empty
if portfolio.empty:
    print("Portfolio DataFrame is empty. Please check your calculations.")
    exit()

# Performance Metrics
rolling_max = portfolio['total'].cummax()
drawdown = portfolio['total'] / rolling_max - 1
max_drawdown = drawdown.min()

print(f"Cumulative Return: {portfolio['cumulative_returns'].iloc[-1]:.2%}")
print(f"Maximum Drawdown: {max_drawdown:.2%}")

# Visualization
plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['MA5'], label='MA5', alpha=0.5)
plt.plot(data['MA10'], label='MA10', alpha=0.5)

# Mark buy and sell signals
plt.plot(data[data['Position'] == 1].index, data['Close'][data['Position'] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, data['Close'][data['Position'] == -1], 'v', markersize=10, color='r', label='Sell Signal')

plt.title('Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# Plot Portfolio Value over Time
plt.figure(figsize=(14,7))
plt.plot(portfolio['total'], label='Portfolio Total Value')
plt.title('Portfolio Performance')
plt.ylabel('Total Portfolio Value ($)')
plt.xlabel('Date')
plt.legend()
plt.show()

# Plot Cumulative Returns
plt.figure(figsize=(14,7))
plt.plot(portfolio['cumulative_returns'], label='Cumulative Returns')
plt.title('Cumulative Returns Over Time')
plt.ylabel('Cumulative Returns')
plt.xlabel('Date')
plt.legend()
plt.show()
