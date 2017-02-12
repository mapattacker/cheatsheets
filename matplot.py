import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

### two main ways to plot
  #1. when dataframe is outside, you can enter arguements inside OR outside brackets.
df.plot()
df.plot(figsize(18,5), legend=True, title='Frasers Centrepoint Trust', label='Adjusted Closing Price')

  #2 when df is inside, arguments must be entered as a separate line.
plt.figure(figsize=(18, 5)) #note this sets for all figures in script
plt.plot(df.index, df['Adj Close'])
plt.title('Frasers Centrepoint Trust')
plt.xlabel('Date')
plt.ylabel('Volume')
