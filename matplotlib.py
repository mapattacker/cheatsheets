import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

### COLORS---------------------------------------
  #normal form
color = red
  #short form
b: blue; g: green r: red c: cyan, m: magenta, y: yellow, k: black, w: white
  # html
color = '#eeefff'


### TWO BASIC WAYS OF PLOTTING---------------------------------------
  #1. when dataframe is outside, you can enter arguements inside OR outside brackets.
df.plot()
df.plot(figsize(18,5), legend=True, title='Frasers Centrepoint Trust', label='Adjusted Closing Price')
top.axes.get_xaxis().set_visible(False)

  #2 when df is inside, arguments must be entered as a separate line.
plt.figure(figsize=(18, 5)) #note this sets for all figures in script
plt.plot(df.index, df['Adj Close'])

plt.title('Frasers Centrepoint Trust')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.ylim([0.01,0.025]) #set x and y axis limits
plt.xlim([-0.003,0.004])

  #subplot settings; have to add set_*
ax1.set_title('CapitalMall Trust')
ax1.set_ylabel('Adj Closing Price')
ax2.set_ylabel('Volume')



### ADD HORIZONTAL/VERTICAL LINE, axhline---------------------------------------
df2.plot(figsize(15,5)).axhline(y = 0, color = "red", lw=1)
    #or just add to a new line
plt.axhline(y = 0, color = "red", lw=1)
plt.axvline(y = 0, color = "red", lw=1) #vertical lines



### ADD ANNOTATIONS---------------------------------------
plt.text('2015-10-23', 2.25, 'SMA 10-20',rotation=90) #(x, y, text, rotate-label)

# http://matplotlib.org/users/annotations_guide.html#plotting-guide-annotation
 # label name, data points, annotation text
    plt.annotate(label, 
                 xy = (x, y), 
                 xytext = (50, 50),
                 textcoords = 'offset points', 
                 ha = 'right', 
                 va = 'bottom',
                 arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3, rad=-0.3'))

    
### SUBPLOTS---------------------------------------
#subplots, equal sizing of each plot
fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 20))
sns.regplot(x=df[df.columns[1]], y='Protected Areas', data=df, ax=ax[0,0])
sns.regplot(x=df[df.columns[2]], y='Protected Areas', data=df, ax=ax[0,1])
sns.regplot(x=df[df.columns[3]], y='Protected Areas', data=df, ax=ax[0,2])
sns.regplot(x=df[df.columns[4]], y='Protected Areas', data=df, ax=ax[1,0])
sns.regplot(x=df[df.columns[5]], y='Protected Areas', data=df, ax=ax[1,1])
sns.regplot(x=df[df.columns[6]], y='Protected Areas', data=df, ax=ax[1,2])

# using subplot2grid; full control over size of each plot
plt.figure(figsize(14,5)) #define plot dimensions
    #arguments: grid dimensions (rows,columns), placement of plot in grid (row, column), no. of rows it occupy, no. columns it occupy.
    #note that even if rowspan=1, dimension is (4,4), you cant put placement as (4,0), but rather (3,0)
top = plt.subplot2grid((5,4), (0, 0), rowspan=3, colspan=3) 
bottom = plt.subplot2grid((5,4), (4,0), rowspan=2, colspan=3)
top.plot(FCT.index, FCT['Adj Close'])
bottom.bar(FCT.index, FCT['Volume'])
