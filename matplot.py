import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# two main ways to plot
  #1. when dataframe is outside, you can enter arguements inside OR outside brackets.
df.plot()
df.plot(figsize(18,5), legend=True, title='This is a title', label='Adjusted Closing Price')

  #2 when df is inside, arguments must be entered as a separate line.
plt.figure(figsize=(18, 5))
plt.plot(df.index, df['Adj Close'])
