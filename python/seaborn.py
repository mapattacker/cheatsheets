import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#------------------------------------------------------------------------------------
# http://gree2.github.io/python/2015/05/05/python-seaborn-tutorial-controlling-figure-aesthetics
# Reset all parameters to default
sns.set()

# STYLES
# default is darkgrid, others include: whitegrid, dark, white
sns.set_style('darkgrid')
sns.set_style('whitegrid')
sns.set_style('dark')
sns.set_style('white')

# SIZE
# default is notebook, others include: paper, talk, poster
sns.set_context('notebook')
sns.set_context('paper')
sns.set_context('talk')
sns.set_context('poster')

# REMOVE BORDER
# only for white & tick styles
# put at bottom of plot
sns.despine() # remove top and right border
sns.despine(left=True, bottom=True) # also remove left and bottom borders


#------------------------------------------------------------------------------------
# COLOR PALETTES
# for entering in argument cmap=...
# http://seaborn.pydata.org/tutorial/color_palettes.html
# http://chrisalbon.com/python/seaborn_color_palettes.html
sns.color_palette() # default palette
sns.color_palette("deep", 10)

# plot out color palettes
 sns.palplot(sns.color_palette("deep", 10))

# see other palette types in links provided.


#----------------------------- PLOTTING GRAPHS --------------------------------------
#------------------------------------------------------------------------------------
  # GRAPH SETTINGS

# add in x & y labels
plt.xlabel('Agricultural Land %', fontsize=18) #change font size too!
plt.ylabel('Protected Areas %')

# change size, put this line in front. 2 is width, 6 is height
# put at start of plot
plt.figure(figsize=(2, 6))

# rotate axis labels
plt.xticks(rotation=90)
#------------------------------------------------------------------------------------
  # MULTIPLE PLOTS

# plot individual columns
sub1=df[['VAR1','VAR2','VAR3']]
sns.boxplot(data=sub1)

# plot individual columns but by one levels of a categoical variable
sub1=df[['CAT1','VAR1','VAR2','VAR3']]
sub1.boxplot(by='CAT1')

#------------------------------------------------------------------------------------
  # SINGLE AXIS GRAPHS
 
# boxplot
  # vertical; if need horizontal change y to x
sns.boxplot(y=df[df.columns[3]]) # dots within box not shown
sns.stripplot(y=df[df.columns[i]], size=4, jitter=True, color="black") # boxes in plot shown

# countplot
sns.countplot(x=df[df.columns[1]], data=df)

# distribution plot
sns.distplot(x=df[df.columns[1]], data=df)

#------------------------------------------------------------------------------------
  # DOUBLE AXES GRAPHS
 
# regression plot & linear model plot
sns.regplot(x=df.columns[7],y='PROTECTED_AREAS_T_M%', data=df)
sns.lmplot(x=df.columns[7],y='PROTECTED_AREAS_T_M%', data=df)
  # add pearson's R
import scipy.stats as ss
ss.pearsonr(df3_layer['depth'],df3_layer['diameter'])

# scatterplot
  # basically same as lmplot & regplot but add a fit_reg=False
sns.lmplot(x=df.columns[7],y='PROTECTED_AREAS_T_M%', fit_reg=False, data=df)
 
# barchart, using factorplot
sns.factorplot(x='NUMBER_LAYERS',y='DEPTH_RIMFLOOR_TOPOG',kind='bar', data=df2)
sns.factorplot(x='layers',y='depth',data=df3, kind='bar', ci=False) # remove confidence interval

## CORRELATION plots
# joinplot, for only pairwise comparison. Gives histograms & scatterplot. Gives correlation labels.
sns.jointplot('CMT', 'FCT', df2, kind='scatter', color='seagreen')
# pairplot, for multiple comparisons. Gives histograms & scatterplots. No correlation labels.
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df3.dropna())
# pairgrid, for multiple comparisons. Define plot type. No correlation labels.
fig = sns.PairGrid(df3.dropna())
  # define top, bottom and diagonal plots
  fig.map_upper(plt.scatter, color='purple')
  fig.map_lower(sns.kdeplot, cmap='cool_d')
  fig.map_diag(sns.distplot, bins=30)
# corrplot, for multiple comparisons. Gives correlation labels.
sns.linearmodels.corrplot(df3.dropna())

corr = df.corr()
plt.figure(figsize=(15, 8))
sns.heatmap(corr, cmap=sns.color_palette("RdBu_r", 20));
  
#------------------------------------------------------------------------------------
  # SUBPLOTS
fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 20))

sns.regplot(x=df[df.columns[1]], y='Protected Areas', data=df, ax=ax[0,0])
sns.regplot(x=df[df.columns[2]], y='Protected Areas', data=df, ax=ax[0,1])
sns.regplot(x=df[df.columns[3]], y='Protected Areas', data=df, ax=ax[0,2])
sns.regplot(x=df[df.columns[4]], y='Protected Areas', data=df, ax=ax[1,0])
sns.regplot(x=df[df.columns[5]], y='Protected Areas', data=df, ax=ax[1,1])
sns.regplot(x=df[df.columns[6]], y='Protected Areas', data=df, ax=ax[1,2])
