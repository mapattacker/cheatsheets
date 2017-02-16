import pandas as pd

## READ & WRITE
    # CSV
df = pd.read_csv('shenzhen_processed.csv')
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)   #take 1st col as index, and remove 1st row
df.to_csv('shenzhen_processed.csv', index=False)
    # EXCEL
df = pd.read_excel('shenzhen_processed.csv')
df.to_excel('output.xlsx', index=False)
    # SQL
conn = sqlite3.connect(sqlitePath) 
df= pd.read_sql_query("SELECT * FROM table", conn)
    # TXT
utown=pd.read_table('university_towns.txt', sep=',', header=None)
    # convert a clip board into dataframe!!!
pd.read_clipboard()

#--------------------------------------------------------
## SETTINGS
pd.set_option('display.max_columns', None) # show all columns
pd.set_option('display.max_rows', None) # show all rows
pd.set_option('display.max_colwidth', -1) # no limit to column width

    # jupyter notebook magic functions
%lsmagic #list all magic
%%timeit -n 100 #time script to complete, -n 100 means only loop 100 times
    
#--------------------------------------------------------
## EXPLORATORY
df.shape #total number of rows by columns
len(df) #total number of rows
len(df.columns) #total number of columns
df.head(2) #top 2 rows
df.dtypes #format
df.describe #mean, std, count, etc. only numeric formated columns

#--------------------------------------------------------
## FORMAT
df.dtypes
df['hour'] = df['hour'].astype('int64')
pd.to_datetime(df2['time'])


#--------------------------------------------------------
## Using SQL
query = ''' SELECT *
            FROM customer
            WHERE first_name = 'MARY'  '''
sql_to_df(query).head()


#--------------------------------------------------------
## INDEX NAMES
df.index
df['country'] = df.index #transfer index to a column
df = df.set_index('Gold') #set index from a column

df = df.set_index(['STNAME', 'CTYNAME']) #can set hierachical index
df.loc['Michigan', 'Washtenaw County'] #querying from index

df = df.reset_index(drop=True) #reset index; drop=True to remove original index as a column

df.loc['Animal'] #index name
df.iloc[5:10] #index location; row number

    #iloc can also detect by both index & column
df.iloc[1,0] #index 1, column 0
df.iloc[:,0] #all index, column 0


# ix indexing works just the same as .loc when passed strings
df.ix[['Andrade']] == df.loc[['Andrade']]
# ix indexing works the same as .iloc when passed integers.
df.ix[[33]] == df.iloc[[33]]

#--------------------------------------------------------
## COLUMNS NAMES
    ## identify column names
df.columns
df.columns[:2] ## first 3 columns
    ## show column names and position
x = 0
for i in df.columns:
    print x, i
    x += 1
    #renaming columns
df2 = df.rename(columns={'diam_circle_image':'diameter','depth_rimfloor_topog':'depth', 'number_layers':'layers'})
hdata2.rename(columns=dict(zip(hdata2.columns,date_change.tolist())), inplace=True) #change two lists into dictionary
df.columns = map(str.lower, df.columns) # change to lower case
    #drop columns
df.drop(df.columns[[0, 1, 3]], axis=1)
df.drop('column_name', axis=1, inplace=True) #note that if inplace value is not set to true, need to reassign a new df
del df['column_name']
    #choose column names by condition
col = [i for i in df.columns if i[-4:]=='2012']

    #concat two lists of columns together
df[df.columns[1:11] | df.columns[12:14]]

#--------------------------------------------------------
## COUNTING
df['EVENT_TYPE'].value_counts()
df['number_layers'].value_counts(normalize=True)*100 # by percentage
df.describe()

#--------------------------------------------------------
## NAN NULL VALUES
    # note that NAN is only for numerical null values
df.isnull().any().any() # is there any nan in entire dataframe? Boolean
df.isnull().values.sum() #total number of nan in dataframe? Value
df.isnull().any() # which column is the nan in? Boolean

for i in df.columns: # how many nan in each column? Value
    print df[i].isnull().values.sum(), i

    #drop NaN
df3 = df2.dropna() #drop all rows with nan in any columns
df.dropna(subset=['x277_2012'],inplace=True) #drop all rows for specific columns

    #fill Nan
df = df.fillna(value=99) #change NaN a value
df = df.fillna(method='ffill') #forward filling, note need to 
index
df = df.fillna(method='bfill') #back filling, note to sort index

    #set value as NaN
import numpy as np
df.replace({'99':np.nan}, inplace=True)

#--------------------------------------------------------
## SORTING
    # sort by index
df.sort_index()
df.sort_values #note no brackets

    # sort by value (column)
df.sort_values(ascending=False)

    # sort 1 column out of many
df2=df[['country','x277_2012']]
df2.sort_values('x277_2012',ascending=False)
    # sort multiple columns
df1.sort_values(['a', 'b'], ascending=[True, False])

#--------------------------------------------------------
## FILTERING, SQL WHERE CLAUSE
df[:100] # first 100 rows
df[df['EVENT_TYPE'] == 'Thunderstorm Wind'] # one value
df[df['A'].str.contains("hello")] # SQL like
df[df['EVENT_TYPE'].isin(['Thunderstorm Wind', 'Hail', 'Winter Weather'])] # multiple values, like an SQL where~in clause

df3 = df2[(df2['layers']>0) & (df2['depth']>0)] # multiple columns using 'AND'
df3 = df2[(df2['layers']>0) | (df2['depth']>0)] # multiple columns using 'OR'


# SQL NOT IN, note the curly '~' which act as a boolean
list = ['WORLD', 'INCOME', 'DEVELOPING']
df = df[~df['country'].isin(list)]
# SQL NOT LIKE OR
list = ['WORLD', 'ALL', 'DEVELOPING', 'ASIA', 'OTHER', 'MEMBERS', 'INCOME', 'DEVELOPED',  \
        'COUNTRIES', 'SITUATIONS', 'EUROPE', 'STATES']
for i in list:
    df = df[~df['country'].str.contains(i)]

#--------------------------------------------------------
## UNIQUE VALUES
df['EVENT_TYPE'].unique() # single column, array
df[['EVENT_TYPE', 'EVENT_ID']].drop_duplicates() # multiple columns, dataframe

#--------------------------------------------------------
## NEW COLUMN CALCAULATIONS
    ## SINGLE COLUMN CONDITION
    ## by summing
df['TOTAL'] = df[df.columns[:]].sum(axis=1)
    ## by function
def timerange(x):
    if x >= 0 and x < 3:
        return '00:00-03:00'
    elif x >= 3 and x < 6:
        return '03:00-06:00'
    else:
        return '21:00-24:00'
df['time_range'] = df['hour'].apply(timerange)

    ## if else using np.where
df['logic'] = np.where(df['AAA'] > 5,'high','low')
    
    # calculating current to one row below
df['new'] = df['Reviewed']-df['Reviewed'].shift()
df['new'] = df['Reviewed'].diff() #this is more straightforward

    ## quartile cut
df3['diameter2'] = pd.qcut(df3.diameter, 2, labels=['<50%','>50%'])
    ## equal interval cut
df3['diameter2'] = pd.cut(df3.diameter, 2, labels=['<50%','>50%'])

df['hour'] = df['time'].str[:2] #select 1st 2 left characters in a string
    ## multiple columns
df3['DIFF_DAY'] = df3['END_DAY']-df3['BEGIN_DAY']

    ##Boolean, contains
df['StatesT']=df['states].str.contains('edit')

    ## calculate new column row by row
for i in range(len(df)):
    x = df[longtidue][i]
    y = df[latitude][i]
    svy = pyproj.transform(wgs84, svy21, x, y)
    df.set_value(i, 'X_svy', svy[0]) #set_value(index, column, value)
    df.set_value(i, 'Y_svy', svy[1])

    
    ## lambda function iterates a simple function. x below refers to each row of Top15{'PopEst']
Top15['PopEst']=Top15['PopEst'].apply(lambda x: "{:,}".format(x))   
df['data']=df['data'].apply(lambda x: 'true' if x <= 2.5 else 'false')

#--------------------------------------------------------
# REPLACE VALUES
    #option 1
dict={4:88, 1:11}
df1['a'].replace(dict,inplace=True)
    #option 2
df['Country'].apply(lambda x: dict.get(x,x))

#--------------------------------------------------------
## GROUP BY AND CALCULATING
census_df[['STNAME', 'COUNTY']].groupby(['STNAME']).sum() #SELECT sum(county), stname FROM tablenm GROUP BY stname
df3.groupby(['longitude', 'latitude']).count()
df3.groupby(['longitude', 'latitude']).sum()

    #group by to show just top 3 records for each STNAME
df.groupby(['STNAME']).head(3)

    #multiple aggregations
Top15.groupby('Continent')['PopEst'].agg({'size': np.count_nonzero, 'mean': np.mean, 'sum': np.sum, 'std': np.std})

#--------------------------------------------------------
## SIMPLE MATHS
max(df['Gold']) #get the max value in the column
new3['CENSUS2010POP'].nlargest(3) #get top 3 by number; note all columns still show
new3['CENSUS2010POP'].nsmallest(3) #get bottom 3 by number

Top15['Avg']=Top15[df.columns[10:]].mean(axis=1) #mean for columns

Top15[['est','cit']].corr() #default is pearson's; give a correlation matrix
# can add method='pearson'

df2=df.pct_change() #difference of each row and the next with percentage. good for calculating stocks daily retuns
sma10 = CMT['Close'].rolling(10).mean() #calcluating moving averages
df.std() #standard deviation

CMT['Adj Close'].quantile(0.75) #get value by quantile, in this case 75%
                 
#--------------------------------------------------------
## BUILDING A DATAFRAME
    #build dataframe from a for loop
x = 0
list = []
for i in df.columns: # how many nan in each column? Value
    list.append({'column':x, 'nan_count':df[i].isnull().values.sum(), 'variable':i})
    x+=1
df_nan = pd.DataFrame(list)

    #create random dataframe
df1 = pd.DataFrame(np.random.randint(1, 5, (10,2)), columns=['a','b']) #10 rows, 2 columns, with numbers 1 to 5

#--------------------------------------------------------
## TRANSPOSING
df.T

#--------------------------------------------------------
## JOINS
# http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#compare-with-sql-join
    #default is inner join
df=pd.merge(df1, df2, on='Country')
hudf=pd.merge(hdf, ul, how ='left', on=['State','RegionName']) #join on multiple columns

    #join by index
df=pd.concat([df1,df2], axis=1, join_axes=[df1.index])

#--------------------------------------------------------
## DATES
    #change string to date format
col = pd.to_datetime(df.columns[6:])
    #aggregation by date intervals
date=date.resample('Q').mean()  #by quarter, also (Day: D, Week: W, Month: M, Quarter: Q, Year: Y)
                 
    #change date to string
date_yr=a['column_nm'].dt.strftime('%Y') #change to year
