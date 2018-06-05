import pandas as pd
import pandas_datareader.data as web
from datetime import datetime


# PARSE DATETIME

#--------------------------------------------------------
## RESAMPLE
    # aggregation by date intervals
    # list of rules can be found in url: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
df.resample(rule='A').mean()

## SOME FUNCTIONS
ford['Volume'].argmax() #returns the index where 1st occurence of max occur. given that index is datetime

## SHIFT


## PERCENTAGE CHANGE; per day
tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1) ) - 1 #OR
tesla['returns'] = tesla['Close'].pct_change(1)

## CUMULATIVE DAILY RETURNS
    # Cumulative return is computed relative to the day investment is made.
tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()


## ROLLING MEAN (OR MOVING AVERAGE)
df['Close'].rolling(window=30).mean()

## EXPANDING
    ## average since start
df['Close'].expanding(min_periods=1).mean()


# BOLLINGER BANDS
    #Developed by John Bollinger, Bollinger Bands are volatility bands placed above and below a moving average. 
    #Volatility is based on the standard deviation, which changes as volatility increases and decreases. 
    #The bands automatically widen when volatility increases and narrow when volatility decreases. 
    #This dynamic nature of Bollinger Bands also means they can be used on different securities with the standard settings. 
    #For signals, Bollinger Bands can be used to identify Tops and Bottoms or to determine the strength of the trend.
df['Close: 30 Day Mean'] = df['Close'].rolling(window=20).mean() #SMA
df['Upper'] = df['Close: 30 Day Mean'] + 2*df['Close'].rolling(window=20).std() #upper band
df['Lower'] = df['Close: 30 Day Mean'] - 2*df['Close'].rolling(window=20).std() #lower band
df[['Close','Close: 30 Day Mean','Upper','Lower']].plot(figsize=(16,6)) #plot