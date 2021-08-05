import pandas as pd
import matplotlib.pyplot as plt
# non interactive, but less heavy
%matplotlib inline 
# prevents default reduction resolution in jupyter notebook
%config InlineBackend.figure_format = 'retina'
# new interactive charts, use plt.figure() tog for a new chart, else will be all in a single one
# sometimes plot will not show, just add another line of %matplotlib notebook
plt.figure()
%matplotlib notebook



### DISABLE DOUBLE PLOTTING BUG---------------------------------------
sm.qqplot(df2['elect_lag']); # add a semi-colon at the end


### SETTINGS---------------------------------------
# see available styles
plt.style.available
plt.style.use('seaborn-white') #set the style

# IMPT!!!!!!
# add a semi-colon to the end of the plotting call to suppress unwanted output
df.plot(); 
# prevents overlapping of axis labels, tick labels and titles
plt.tight_layout()
# fix fig/font size & DPI for entire jupyter notebook & script
plt.rcParams["figure.figsize"] =(10,10)
plt.rcParams.update({'font.size': 4})
plt.rcParams['figure.dpi'] = 300


### COLORS---------------------------------------
  #normal form
color = red
  #short form
b: blue; g: green r: red c: cyan, m: magenta, y: yellow, k: black, w: white
  # html
color = '#eeefff'

  #color maps; cmap
  # https://matplotlib.org/tutorials/colors/colormaps.html
cmaps['Qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']

cmaps['Miscellaneous'] = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']

### OTHERS---------------------------------------
  #line thickness
plt.plot([1,50], [0,20], linewidth=10)
  #show gridlines
    # only major grids
plt.grid() 
    # show major & minor grids
plt.grid(b=True, which='major')
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)
  #interpolations for imshow of images
  # https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html
plt.imshow(image, interpolation='nearest')

  #marker type
  #https://matplotlib.org/3.1.0/api/markers_api.html
# 's' = square
# '.' = dot
# 'x' = cross


### CLEARING CHARTS---------------------------------------
plt.cla() #clears an axis, i.e. the currently active axis in the current figure. It leaves the other axes untouched.
plt.clear() #clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots.
plt.close() #closes a window, which will be the current window, if not specified otherwise.

hline = plt.axhline(y = line, color = "red", lw=1)
hline.remove() #remove an object in the chart

# remove x & y axes
plt.axis('off')

# refresh chart
maxiter = 10
for i in range(maxiter):
  plot_something(x, y, best_tour, tau)
  plt.pause(0.25)
  if i != maxiter-1:
      plt.close()
  else:
      plt.show()


### SAVE CHART IMAGE---------------------------------------
plt.plot(range(10))
plt.savefig('testplot.png', dpi=300) #save as png

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
plt.plot(df.index, df['Adj Close']);

  #title
plt.title('Frasers Centrepoint Trust', fontsize=10)
  #axis title
plt.xlabel('Date', fontsize=10)
plt.ylabel('Volume', fontsize=10)
  #axis angle or orientation
plt.xticks(x, labels, rotation='vertical')
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
           title='Chiller No.',
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
#e.g. 1 --------
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


#e.g. 2 --------
fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(15, 8))

axis1 = [0,0,1,2,3,4,5]
axis2 = [0,0,1,2,3,4]

ax[0,0].plot(axis1, cosine_pca);
ax[0,1].plot(axis1, cosine_pca_eo);
ax[0,2].plot(axis2, cosine_pca_nc);
ax[1,0].plot(axis2, cosine_pca_fwc);
ax[1,1].plot(axis2, cosine_pca_fwe);
ax[1,2].plot(axis2, cosine_pca_rl);

# subtitles
ax[0,0].title.set_text('Condenser Fouling')
ax[0,1].title.set_text('Excess Oil')
ax[0,2].title.set_text('Non Condensables')
ax[1,0].title.set_text('Reduce Condenser Water Flow')
ax[1,1].title.set_text('Reduce Evaporator Water Flow')
ax[1,2].title.set_text('Refrigerant Leak')

# main title
fig.suptitle('PCA > Cosine Similarity', y=1.05, size=15)
plt.tight_layout()

#e.g. 3 --------
# create a 3x3 grid of subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
# plot the linear_data on the 5th subplot axes 
ax5.plot(linear_data, '-')



### SUBPLOT2GRID-------------------------------------------------------------------------
# advantage of subplot2grid: full control over size of each plot
plt.figure(figsize=(14,5)) #define plot dimensions
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
# https://riptutorial.com/matplotlib/example/20875/multiple-plots-with-gridspec
# gs[row_space:column_space]
# define by list slicing
import matplotlib.gridspec as gridspec
plt.figure(figsize=(8,8))
gs = gridspec.GridSpec(4,4)
plt.subplot(gs[:, 0:3])
plt.subplot(gs[0:1,3:4])
plt.subplot(gs[1:2:,3:4])
plt.subplot(gs[2:3:,3:4])
plt.subplot(gs[3:4,3:4])
plt.tight_layout()


#               plot 1
# ---------------------------------   ---------
# |                                | |         |
# |                                | |         | plot 2
# |                                | |         |
# |                                |  ---------
# |                                |  ---------
# |                                | |         |
# |                                | |         | plot 3
# |                                | |         |
# |                                |  ---------
# |                                |  ---------
# |                                | |         |
# |                                | |         | plot 4
# |                                | |         |
# |                                |  ---------
# |                                |  ---------
# |                                | |         |
# |                                | |         | plot 5
# |                                | |         |
# ---------------------------------   ---------

### CHART TYPES--------------------------------------------------------------------------
  # line-plot
plt.plot(x, y)
  # scatter-plot
plt.scatter(dfinal['day'], dfinal['tmax15'], s=5, c='r')
  # histogram
plt.hist(sample, bins=100, orientation='horizontal')
  # bar-plot
plt.bar(FCT.index, FCT['Volume'])
  # horizontal bar-plot
plt.hbar(FCT.index, FCT['Volume'])
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


### 3D PLOTS---------------------------------------
from mpl_toolkits.mplot3d import Axes3D

  # scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_pca[0], x_pca[1], x_pca[2], c=labels, cmap='viridis', s=40);



### LIVE REFRESH IN NOTEBOOK---------------------------------------
# live update of charts when using a for loop

from IPython import display
from matplotlib import pyplot as plt
%matplotlib inline 
%config InlineBackend.figure_format = 'retina'

for i in range(x):
  plt.gca().cla() # clear legend else it will culmulate
  plt.plot(epoch_list_al, label="AL")
  plt.plot(epoch_list_rdm, label="RDM")
  plt.legend()
  display.display(plt.gcf())
  display.clear_output(wait=True)
  time.sleep(0.5)