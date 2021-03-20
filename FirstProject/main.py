import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.data import Options
import datetime
import quandl as qd
import numpy as np
import seaborn as sns
from numpy import random as rand
from datetime import datetime

mcdon = pd.read_csv(r'C:\Users\wwstudent\PycharmProjects\FirstProject\walmart_stock.csv', index_col='Date', parse_dates=True)
mcdon.to_csv('mcdon')

# print(mcdon.head())

# print(mcdon['Open'].plot())

# mcdon.autofmt_xdate()
# Fixes date overlap

# Quandl and Pandas data read to return stock data

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2017, 1, 1)

facebook = web.DataReader('FB', 'yahoo', start, end)
print(facebook.head())

# Retrieving Options # Does not work with pandas data reader now
# fb_options = Options('FB', 'yahoo')
# options_df = fb_options.get_option_data(expiry=fb_options.expiry_dates[0])

#  print(options_df.head())

# QUANDL DATA

# API KEY xTzvuioJE_zdPUfBc9Yf

qd.ApiConfig.api_key = 'xTzvuioJE_zdPUfBc9Yf'

RealEstate = qd.get('ZILLOW/DATA', start_date='2021, 1, 1', end_date='2021, 3, 17')

print(RealEstate)

# mydata = qd.get("WIKI/APPL")

# print(mydata.head())

# TIME SERIES
