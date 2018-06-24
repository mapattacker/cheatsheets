import pandas as pd
import matplotlib.pyplot as plt
# non interactive, but less heavy
%matplotlib inline 
# new interactive charts, use plt.figure() tog for a new chart, else will be all in a single one
plt.figure()
%matplotlib notebook


### SETTINGS---------------------------------------
# see available styles
plt.style.available
plt.style.use('seaborn') #set the style

# IMPT!!!!!!
# add a semi-colon to the end of the plotting call to suppress unwanted output
df.plot(); 
# prevents overlapping of axis labels, tick labels and titles
plt.tight_layout()
# fix figsize for entire jupyter notebook
plt.rcParams["figure.figsize"] =(10,10)


### COLORS---------------------------------------
  #normal form
color = red
  #short form
b: blue; g: green r: red c: cyan, m: magenta, y: yellow, k: black, w: white
  # html
color = '#eeefff'


### OTHERS---------------------------------------
  #line thickness
plt.plot([1,50], [0,20], linewidth=10)
  #show gridlines
plt.grid()
  #interpolations for imshow of images
  # https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html
plt.imshow(image, interpolation='nearest')


### CLEARING CHARTS---------------------------------------
plt.cla() #clears an axis, i.e. the currently active axis in the current figure. It leaves the other axes untouched.
plt.clear() #clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots.
plt.close() #closes a window, which will be the current window, if not specified otherwise.

hline = plt.axhline(y = line, color = "red", lw=1)
hline.remove() #remove an object in the chart

# remove x & y axes
plt.axis('off')

### SAVE CHART IMAGE---------------------------------------
plt.plot(range(10))
plt.savefig('testplot.png') #save as png

import Image
Image.open('testplot.png').save('testplot.jgp', 'JPEG') #save as jpeg using Pillow

### TWO BASIC WAYS OF PLOTTING---------------------------------------
  #1. Plotting Using Pandas
  # when dataframe is outside, you can enter arguements inside OR outside brackets.
df.plot()
df.plot(figsize(18,5), legend=True, title='Frasers Centrepoint Trust', label='Adjusted Closing Price')
top.axes.get_xaxis().set_visible(False)

  #2. Plotting using Matplotlib 
  # when df is inside, arguments must be entered as a separate line.
plt.figure(figsize=(18, 5)) #note this sets for all figures in script
plt.plot(df.index, df['Adj Close'])

  #title
plt.title('Frasers Centrepoint Trust', fontsize=10)
  #axis title
plt.xlabel('Date', fontsize=10)
plt.ylabel('Volume', fontsize=10)
  #axis tick intervals
plt.xticks(np.arange(-180.0, 200, 45.0)) #max, min, interval
  #axis tick size
plt.xticks(size = 10)
plt.yticks(size = 10)
  #axis scale limits
plt.ylim([0.01,0.025]) #set x and y axis limits
plt.xlim([-0.003,0.004])
  #log scaling
plt.xscale('log')
plt.yscale('log')
  #change axis position
plt.yaxis.tick_right()
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


### SUBPLOTS-----------------------------------------------------------------------------
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

# or use simple iteration if rows=1 or cols=1
fig, ax = plt.subplots(ncols=9, nrows=1, figsize=(20, 15))
for i, a in enumerate(ax):
    a.imshow(images[i])

# if col & row>1, flatten nested axes list so can iterate
fig, axes = plt.subplots(ncols=2, nrows=4, figsize=(10, 10))
a = [i for i in axes for i in i]
for i, ax in enumerate(a):
    ax.imshow(eroded[i], 'gray');

#e.g. 2
# create a 3x3 grid of subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
# plot the linear_data on the 5th subplot axes 
ax5.plot(linear_data, '-')


### SUBPLOT2GRID-------------------------------------------------------------------------
# advantage of subplot2grid: full control over size of each plot
plt.figure(figsize(14,5)) #define plot dimensions
    #arguments: grid dimensions (rows,columns), placement of plot in grid (row, column), no. of rows it occupy, no. columns it occupy.
    #note that even if rowspan=1, dimension is (4,4), you cant put placement as (4,0), but rather (3,0)
top = plt.subplot2grid((5,4), (0, 0), rowspan=3, colspan=3) 
bottom = plt.subplot2grid((5,4), (4,0), rowspan=2, colspan=3)
top.plot(FCT.index, FCT['Adj Close'])
bottom.bar(FCT.index, FCT['Volume'])

# set the labels
top.axes.get_xaxis().set_visible(False)
top.set_title('CapitalMall Trust')
top.set_ylabel('Adj Closing Price')
bottom.set_ylabel('Volume')


### GRIDSPEC-------------------------------------------------------------------------
# http://matplotlib.org/users/gridspec.html
# similar to subplot2grid
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1,:-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])



### CHART TYPES--------------------------------------------------------------------------
  # scatter-plot
plt.scatter(dfinal['day'], dfinal['tmax15'], s=5, c='r')
  # histogram
plt.hist(sample, bins=100, orientation='horizontal')
  # bar-plot
plt.bar(FCT.index, FCT['Volume'])
  # boxplot
plt.boxplot([df['normal'], df['random'], df['gamma']])
  # heatmap
plt.hist2d(X, Y, bins=25)
plt.colorbar() #add color range legend
  # error bars
plt.errorbar(x, y, xerr=0.2)


# OR.... use kind = graph_type
plt(kind=bar, x, y)


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


