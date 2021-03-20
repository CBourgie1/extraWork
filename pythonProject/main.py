import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime
from pandas.plotting import scatter_matrix

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2020, 1, 1)

tesla = web.DataReader('TSLA', 'yahoo', start, end)
ford = web.DataReader('F', 'yahoo', start, end)
gm = web.DataReader('GM', 'yahoo', start, end)


print(gm.head())
print(ford.head())
print(tesla.head())

tesla['Open'].plot(label='TESLA', figsize=(12, 8), title='Opening Price')
gm['Open'].plot(label='GM')
ford['Open'].plot(label="Ford")
plt.legend()
print(plt.show())

tesla['Volume'].plot(label='TESLA', figsize=(12, 8), title='Volume Traded')
gm['Volume'].plot(label='GM')
ford['Volume'].plot(label="Ford")
plt.legend()
print(plt.show())

ford['Volume'].argmax()

ford['Volume'].plot(figsize=(20, 6))

tesla['Total Tradein'] = tesla['Open']*tesla['Volume']
ford['Total Tradein'] = ford['Open']*ford['Volume']
gm['Total Tradein'] = gm['Open']*gm['Volume']

tesla['Total Tradein'].plot(label='tesla', title='Market Cap')
ford['Total Tradein'].plot(label='ford')
gm['Total Tradein'].plot(label='gm')
plt.legend()

print(plt.show())

tesla['Total Tradein'].argmax()


gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm["Open"].rolling(200).mean()
gm[['Open', 'MA50', 'MA200']].plot(figsize=(20, 6))
print(plt.show())

car_comp = pd.concat([tesla['Open'], gm['Open'], ford['Open']], axis=1)
car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']
print(car_comp.head())

scatter_matrix(car_comp, figsize=(8, 8), alpha=0.2, hist_kwds={'bins': 50})
plt.show()

# Daily Return
tesla['return'] = (tesla['Close'] / tesla['Close'].shift(1)) - 1
tesla['return'] = tesla["Close"].pct_change(1)
ford['return'] = ford["Close"].pct_change(1)
gm['return'] = gm["Close"].pct_change(1)


ford['return'].hist(100)
gm['return'].gm(100)
tesla['return'].tesla(100, label='tesla', figsize=(10, 8), alpha=0.4)
gm['return'].tesla(100, label='gm', figsize=(10, 8), alpha=0.4)
ford['return'].tesla(100, label='ford', figsize=(10, 8), alpha=0.4)
plt.legend()
plt.show()

# Kernel Density Estimation Plot (Stablility)
tesla['return'].plot(kind='kde', lable='Tesla', figsize=(10, 8))
ford['return'].plot(kind='kde', lable='ford', figsize=(10, 8))
gm['return'].plot(kind='kde', lable='gm', figsize=(10, 8))

# Volatility on daily returns
box_df = pd.concat(tesla['return'], ford['return'], gm['return'], axis=1)
box_df.columns = ['Tesla Ret', 'Ford Ret', 'GM Ret']
box_df.plot(kind='box', figsize=(10, 8))


