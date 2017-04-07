import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
%matplotlib notebook

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

  #title
plt.title('Frasers Centrepoint Trust', fontsize=10)
  #axis title
plt.xlabel('Date', fontsize=10)
plt.ylabel('Volume', fontsize=10)
  #axis tick size
plt.xticks(size = 10)
plt.yticks(size = 10)
  #axis scale limits
plt.ylim([0.01,0.025]) #set x and y axis limits
plt.xlim([-0.003,0.004])
  #legend
plt.legend(loc=9, labels=['Max Temp 2005-2014', 'Min Temp 2005-2014', 'Max Temp 2015', 'Min Temp 2015'], \
           frameon=False, fontsize=6, ncol=4) #ncol, split into horizontal, #loc is location of title



### SUBPLOT-----------------------------------------------------------------------------
plt.figure()
ax1 = plt.subplot(1, 2, 1) #arg(nrow, ncol, 1st plot)
plt.plot(linear_data, '-o')
# pass sharey=ax1 to ensure the two subplots share the same y axis
ax2 = plt.subplot(1, 2, 2, sharey=ax1) #arg(nrow, ncol, 2nd plot), share axis with 1st plot
plt.plot(exponential_data, '-x')

  #subplot settings; have to add set_*
ax1.set_title('CapitalMall Trust')
ax1.set_ylabel('Adj Closing Price')
ax2.set_ylabel('Volume')


### SUBPLOTS---------------------------------------
#advantage of subplot: easier to control all figures
#e.g. 1
#subplots, equal sizing of each plot
fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 20))
sns.regplot(x=df[df.columns[1]], y='Protected Areas', data=df, ax=ax[0,0])
sns.regplot(x=df[df.columns[2]], y='Protected Areas', data=df, ax=ax[0,1])
sns.regplot(x=df[df.columns[3]], y='Protected Areas', data=df, ax=ax[0,2])
sns.regplot(x=df[df.columns[4]], y='Protected Areas', data=df, ax=ax[1,0])
sns.regplot(x=df[df.columns[5]], y='Protected Areas', data=df, ax=ax[1,1])
sns.regplot(x=df[df.columns[6]], y='Protected Areas', data=df, ax=ax[1,2])

#e.g. 2
# create a 3x3 grid of subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
# plot the linear_data on the 5th subplot axes 
ax5.plot(linear_data, '-')


### SUBPLOT2GRID---------------------------------------
# advantage of subplot2grid: full control over size of each plot
plt.figure(figsize(14,5)) #define plot dimensions
    #arguments: grid dimensions (rows,columns), placement of plot in grid (row, column), no. of rows it occupy, no. columns it occupy.
    #note that even if rowspan=1, dimension is (4,4), you cant put placement as (4,0), but rather (3,0)
top = plt.subplot2grid((5,4), (0, 0), rowspan=3, colspan=3) 
bottom = plt.subplot2grid((5,4), (4,0), rowspan=2, colspan=3)
top.plot(FCT.index, FCT['Adj Close'])
bottom.bar(FCT.index, FCT['Volume'])


### ADD HORIZONTAL/VERTICAL LINE, axhline---------------------------------------
df2.plot(figsize(15,5)).axhline(y = 0, color = "red", lw=1)
    #or just add to a new line
plt.axhline(y = 0, color = "red", lw=1)
plt.axvline(y = 0, color = "red", lw=1) #vertical lines



### ADD ANNOTATIONS---------------------------------------
plt.text('2015-10-23', 2.25, 'SMA 10-20',rotation=90) #(x, y, text, rotate-label)

# http://matplotlib.org/users/annotations_guide.html#plotting-guide-annotation
 # label name, data points coord, annotation text coord, textcoords???, horizontal alignment, vertical alignment, arrow settings
    plt.annotate(label, 
                 xy = (x, y), 
                 xytext = (50, 50),
                 textcoords = 'offset points', 
                 ha = 'right', 
                 va = 'bottom',
                 arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3, rad=-0.3'))

    
