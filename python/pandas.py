import pandas as pd

## READ & WRITE
    # Pickle
df = pd.read_pickle('psi.pickle')
    # CSV
df = pd.read_csv('shenzhen_processed.csv', low_memory=False)
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)   #take 1st col as index, and remove 1st row
df.to_csv('shenzhen_processed.csv', index=False) #
df = pd.read_csv(file, usecols=[0,2])   #use only specific columns
    # EXCEL
    # reading excel has various differences compared to csv
    # dtype of a col to str will convert NaN into 'nan', while csv preserves the NaN
    # dtype of a col to str will not preserve numeric 0 padding, while csv preserves
df = pd.read_excel('shenzhen_processed.xlsx', sheet_name=1) #sheetname starts from 0
df = pd.read_csv("P00000001-ALL.csv", nrows=20) # limit to only 20 rows
df.to_excel('output.xlsx', index=False)
    # output multiple df in different Excel sheets
from pandas import ExcelWriter
writer = ExcelWriter(xls_path)
for n, df in enumerate(list_dfs):
    df1.to_excel(writer,'sheet%s' % n)
writer.save()
    # TXT
utown=pd.read_table('university_towns.txt', sep=',', header=None)
df1 = pd.read_table('training_text', sep='\|\|', engine='python', skiprows=1, names=["ID","Text"]) #note that any delimiter more than 1 is a reg, have to use \ to override
    # convert a clip board into dataframe!!!
pd.read_clipboard()
    # JSON
df=pd.read_json(path)
df.to_json('/Users/xxx/Desktop/d.json')
    #DBF
from simpledbf import Dbf5
dbf = Dbf5('test.dbf')
df = dbf.to_dataframe()
    # Sample the data to speed up computation
df = df.sample(frac=0.1, random_state=10)

# set column as string
df = pd.read_csv('sample.csv', dtype={'ID': object}) #no diff if you '' the data type

# encoding error, eg: 'utf-8' codec can't decode byte 0x92 in position 763: invalid start byte
# use below to decode
df = pd.read_csv(email, encoding = "ISO-8859-1")


#--------------------------------------------------------
## SETTINGS
pd.set_option('display.max_columns',1) # expand column height
pd.set_option('display.max_rows', None) # show all rows
pd.set_option('display.max_colwidth', -1) # no limit to column width
pd.reset_option('all') # reset set options



#--------------------------------------------------------
## PERFORMANCE
df.info(memory_usage="deep") # display memory usage
df.memory_usage(deep=True) # display memory usage for each column

# filter dataframe to select certain dtype
df_obj = df.select_dtypes(include=['object'])

# determining optimal dtype so that memory usage is minimised
df['columnNm'] = pd.to_numeric(df['columnNm'], downcast='integer')
df['columnNm'].dtype

# convert objects into category to minimise memory usage as its converted to int backend
# only use this when unique values <50% of rows & that there is no need for numeric calculations
df['columnNm'] = df['columnNm'].astype('category')


#--------------------------------------------------------
# display html
from IPython.core.display import display, HTML
html = 'https://github.com/PAIR-code/facets/blob/master/facets_dive/Dive_demo.ipynb'
display(HTML(html), width=400)


#--------------------------------------------------------
# jupyter notebook magic functions
%lsmagic #list all magic
%%timeit -n 100 #time script to complete, -n 100 means only loop 100 times; default is 100
%time #time just once with CPU time outputs
%%bash #run bash commands in mac
%%cmd #run command prompt in windows


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

    #from a dictionary
df = pd.DataFrame()
newdf['Date'] = x.keys()    #where x is a dictionary
df['DateValue'] = x.values()

    # build a df with just one row of data. Note the nested list to change it to row
prediction = pd.DataFrame([[4, 21, 1, 5, 91,1984]], \
                          columns=['flat_type_code','town_code','flat_model_code', \
                                   'storey_range_code','floor_area_sqm', 'lease_commence_date'])

    #duplicate a dataframe
df2 = df.copy()


#--------------------------------------------------------
## EXPLORATORY
df.shape #total number of rows by columns
df.size #total number of rows
len(df) #total number of rows too
len(df.columns) #total number of columns
df.head(2) #top 2 rows
df.dtypes #format
df.describe #mean, std, count, etc. only numeric formated columns


#--------------------------------------------------------
## FORMAT
df.dtypes
df['hour'] = df['hour'].astype('int64')
df['text'] = df['text'].astype('str') # string will not preserve NaN, unlike object
df['col3'] = df['col2'].astype('category') # category type has int code in the backend
    #coerce, any errors will be converted to NaN
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')


#--------------------------------------------------------
## Using SQL
    
# Connection to database
    # sqlite connection
import sqlite3
conn = sqlite3.connect(sqlitePath) 
df= pd.read_sql_query("SELECT * FROM table", conn)
    # postgres connection
import psycopg2 
conn = psycopg2.connect(database="postgres", user="postgres", password="***", host="127.0.0.1", port="5432")
    # OR use sqlalchemy, which supports most databases
    # database engine + database connector package://username:password @ host ip / database? client encoding
    # latin1 or utf8 depending on client encoding
from sqlalchemy import create_engine
import psycopg2
conn = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/postgres?client_encoding=latin1') # postgres
conn = create_engine('mysql+pymysal://{}:{}@{}:{}/{}'.format(username, password, address, port, db_name)) # mysql 
query = ''' SELECT * FROM customer  '''

# reading from sql
df = pd.read_sql(query, conn)
df = pd.read_sql_query(query, conn)

# upload dataframe to database as new table by default (use if_exist for appending), only available using sqlalchemy as engine
# if_exists can 'replace' entire table, default is fail
df.to_sql(name='wsg_ap_list3', con=conn, index=False, if_exists='append') #OR
df.to_sql('pa', conn, if_exists='append', index=False, dtype='text')


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
df.columns = ['newcolumn1', 'newcolumn2', 'newcolumn3'] #easiest way to change, but error if total columns does not match
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

    #ordering columns in a df
df[sorted(df.columns.tolist())].head(3)
    #specific ordering of columns
df = df[['a', 'b', 'd', 'c']]


#--------------------------------------------------------
## SET VALUES PER CELL, GOOD FOR ITERATION
df.set_value(i, 'Y_svy', svy[1]) # index, column name, value

# new alternative
df.at[4, 'B'] = 10 # index, column name = value
df.at[4, 'B'] #querying a cell
>>> 10

#--------------------------------------------------------
## COUNTING
df['EVENT_TYPE'].value_counts()
df.groupby('name')['activity'].value_counts() #multi-dimension counts 
df['number_layers'].value_counts(normalize=True)*100 # by percentage
df.describe()


#--------------------------------------------------------
## NAN NULL VALUES
    # note that NAN is only for numerical null values
df.isnull().any().any() # is there any nan in entire dataframe? Boolean
df.isnull().values.sum() #total number of nan in dataframe? Value
df.isnull().any() # which column is the nan in? Boolean
df[df['Timestamp'].isnull()] #filter rows with nan

for i in df.columns: # how many nan in each column? Value
    print df[i].isnull().values.sum(), i

    #filter dataframe to only rows NaN of a specific column
df[df['colnm'].isnull()]

    #drop NaN
df3 = df2.dropna() #drop all rows with nan in any columns
df3 = df2.dropna(how='all') #drop only rows with all nan values
df3 = df2.dropna(threa=2) #drop only rows with 2 or more nan values
df.dropna(subset=['x277_2012'],inplace=True) #drop all rows for specific columns

    #fill NaN
df = df.fillna(value=99) #change NaN a value
df = df.fillna(method='ffill') #forward filling, note need to sort index
df = df.fillna(method='bfill') #back filling, note to sort index

    #set value as NaN
import numpy as np
df2=df2.replace('nan',np.nan)
df.replace({'99':np.nan}, inplace=True) #multiple rows

    #select null within lambda
df['colnm'] = df['colnm'].apply(lambda x: '' if pd.isnull(x)) else x)


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
df3[['a','b']].sort_values(['a','b'], ascending=[True, True]) # sort a first then b


#--------------------------------------------------------
## ENCODING
encode = {'Y':0, 'N':1}
df['Hired'] = df['Hired'].map(encode)


#--------------------------------------------------------
## STRING MANIPULATIONS
    
df['column1'].str.len() # length of each cell
df['column1'].str.strip() # remove spacing front & back. such spaces is not visible in dataframe

# regular expressions is also enabled here
df['text'].str.count(r'\d') # find how many times a digit occurs in each string
df['text'].str.findall(r'(\d?\d):(\d\d)') # group and find the hours and minutes
df['text'].str.replace(r'\w+day\b', '???') # replace weekdays with '???'
df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3]) # replace weekdays with 3 letter abbrevations
    # Extract match to new columns
df['text'].str.extract(r'(\d?\d):(\d\d)') # create new columns from first match of extracted groups
df['text'].str.extractall(r'((\d?\d):(\d\d) ?([ap]m))') # extract the entire time, the hours, the minutes, and the period
df['text'].str.extractall(r'(?P<time>(?P<hour>\d?\d):(?P<minute>\d\d) ?(?P<period>[ap]m))') # extract the entire time, the hours, the minutes, and the period with group names


#--------------------------------------------------------
## FILTERING, SQL WHERE CLAUSE
df[:100] # first 100 rows
df[df['EVENT_TYPE'] == 'Thunderstorm Wind'] # one value
df[df['A'].str.contains("hello")] # SQL like; cannot use if there are NaN values
df[df['EVENT_TYPE'].isin(['Thunderstorm Wind', 'Hail', 'Winter Weather'])] # multiple values, like an SQL where~in clause

# Multiple Conditions, add parenthensis ()!
df3 = df2[(df2['layers']>0) & (df2['depth']>0)] # multiple columns using 'AND'
df3 = df2[(df2['layers']>0) | (df2['depth']>0)] # multiple columns using 'OR'

# REMOVE ROWS
df = df[df['Rating'] != 3]

# SQL NOT IN, note the curly '~' which act as a boolean
list = ['WORLD', 'INCOME', 'DEVELOPING']
df = df[~df['country'].isin(list)]
# SQL NOT LIKE OR
list = ['WORLD', 'ALL', 'DEVELOPING', 'ASIA', 'OTHER', 'MEMBERS', 'INCOME', 'DEVELOPED',  \
        'COUNTRIES', 'SITUATIONS', 'EUROPE', 'STATES']
for i in list:
    df = df[~df['country'].str.contains(i)]

# FILTER ROWS WITH NAN
df[df['mgmtsalary'].isnull()]

# FILTER ROWS WITHOUT NAN
df[df['mgmtsalary'].notnull()]

# CHECK FOR ALPHA OR NUMERIC
df[colnm].str.isnumeric()
df[colnm].str.isalpha()

#--------------------------------------------------------
# set values within a for loop
for i in range(len(df)):
    x = df[longtidue][i]
    y = df[latitude][i]
    svy = pyproj.transform(wgs84, svy21, x, y)
    df.set_value(i, 'X_svy', svy[0]) # row_no, column_nm, value
    df.set_value(i, 'Y_svy', svy[1])

# set value for single cell
df = df.set_value(100, 'colnm', 'value') # row_no, column_nm, value

#--------------------------------------------------------
## UNIQUE VALUES, DUPLICATES
df['EVENT_TYPE'].unique() # single column, array
    # multiple columns, dataframe
df[['EVENT_TYPE', 'EVENT_ID']].drop_duplicates() 
    # set for entire dataframe but target specific columns
df.drop_duplicates(subset=['col1', 'col2'])
df.drop_duplicates(subset=['A', 'C'], keep=False)
df[df.duplicated(keep=False)] # show all duplicated rows (only)

# comparing duplicates between two columns
df[df['States'].ne(df['Region'])]

#group by, add a new count field for duplicate counts
df1 = pd.DataFrame(np.random.randint(1, 15, (100,4)), columns=['a','b','c','d'])
df1.groupby(df1.columns.tolist()).size().reset_index().rename(columns={0:'count'})

    # sometimes, might need to change all to str first as nulls are interferring w groupby
df2 = (df.astype('str').groupby(df.columns.tolist()).size()
         .sort_values(ascending=False)
         .reset_index()
         .rename(columns={0:'duplicates'})
         .replace('nan',np.nan)) #set nulls back to NaN


#--------------------------------------------------------
## DROP ROW
    # by index
df = df.drop(df.index[2938])


#--------------------------------------------------------
## NEW COLUMN CALCAULATIONS
    ## SINGLE COLUMN CONDITION
    ## by summing
df['TOTAL'] = df[df.columns[:]].sum(axis=1)

    ## by function, single column condition
def timerange(x):
    if x >= 0 and x < 3:
        return '00:00-03:00'
    elif x >= 3 and x < 6:
        return '03:00-06:00'
    else:
        return '21:00-24:00'
df['time_range'] = df['hour'].apply(timerange, axis=1)

    ## MULTIPLE COLUMN CONDITION
def peak(x):
    if x['Public Holiday'] == 'National Day' or x['Public Holiday'] == 'New Year''s Day':
        return 'Super Peak'
    if x['dow'] == 'Sunday' or x['dow'] == 'Saturday' or x['dow'] == 'Friday':
        return 'Peak'
    else: 
        return 'Non-Peak'
df3['day_period'] = df3.apply(peak, axis=1)


    ## lambda function iterates a simple function. x below refers to each row of Top15{'PopEst']
    ## Note that lambda must contain if-else when using condition
Top15['PopEst']=Top15['PopEst'].apply(lambda x: "{:,}".format(x))   
df['data']=df['data'].apply(lambda x: 'true' if x <= 2.5 else 'false')
df['date'] = df['raw'].str.extract('(....-..-..)', expand=False) #note that expand will split it into different columns
    #for this case x refers to the entire dataframe, you have to specify the column within the function.
    #this gives if else conditions from multiple columns
    #have to include axis=1 or will prompt error
ticketcat['funpass_days'] = ticketcat.apply(lambda x: '2' if x['ItemDescription'].find('2Day')>=0 else x['funpass_days'],axis=1)


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


    ## regex
df['date'] = df['raw'].str.extract('(....-..-..)', expand=True)
# 0    2014-12-23
# 1    2010-02-23
# 2    2014-06-20
# 3    2014-03-14       
             
    ## split by delimiter
# example of value 'Online,Sales,Adult'
ticketcat['sales'] = ticketcat['TicketDescription'].apply(lambda x: x.split(',')[1])
ticketcat['medium'] = ticketcat['TicketDescription'].apply(lambda x: x.split(',')[0])

    ## using numpy, if > 3, x=1 else x=0
df['Positively Rated'] = np.where(df['Rating'] > 3, 1, 0)


    ## remove words duplicate, assuming there is a delimiter of '|' btw words
def removedup(x):
    x = x.split('|')
    x = set(x)
    x = '|'.join(x)
    return x

df['colnm'] = df['colnm'].apply(removedup)
df['colnm'] = df['colnm'].apply(lambda x: '|'.join(set(x.split('|')))) #alternatively

                 
#--------------------------------------------------------
# SHIFT COLUMN VALUES UP OR DOWN; LAG OR LEAD
df['temp_observed'] = df['temp_observed'].shift(periods=1) #push column down by a row
df['temp_observed'] = df['temp_observed'].shift(periods=-1) #push column up by a row


#--------------------------------------------------------
# REPLACE VALUES
    #option 1: single value
df = df.replace('value1', 'value2')
    #option 2: multiple values
dict={4:88, 1:11}
df1['a'].replace(dict,inplace=True)
    #option 3
df['Country'].apply(lambda x: dict.get(x,x))
    #option 4: replace part of string in value
ticketcat['price']=ticketcat['price'].str.replace('$', '')


#--------------------------------------------------------
# CONFUSION MATRIX
pd.crosstab(df['target'], df['predicted'])


#--------------------------------------------------------
## GROUP BY AND CALCULATING
census_df[['STNAME', 'COUNTY']].groupby(['STNAME']).sum() #SELECT sum(county), stname FROM tablenm GROUP BY stname
df3.groupby(['longitude', 'latitude']).count() #shows all column counts
df3.groupby(['longitude', 'latitude']).sum()
df.groupby(['LocationDescription','LocationCode']).size() #size include NAN counts, counts() does not, shows row size instead of columns

    #group by to show just top 3 records for each STNAME
df.groupby(['STNAME']).head(3)

## GROUPBY AGGREGATIONS 
# https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.core.groupby.DataFrameGroupBy.agg.html

    #multiple aggregations
Top15.groupby('Continent')['PopEst'].agg({'size': np.count_nonzero, 'mean': np.mean, 'sum': np.sum, 'std': np.std})

    #merge nearly duplicate rows based on column value
    # https://stackoverflow.com/questions/36271413/pandas-merge-nearly-duplicate-rows-based-on-column-value
df.groupby(['Name','Sid','Revenue'])['Use_Case'].apply(''.join).reset_index()
df.groupby('Name').agg({'Sid':'first', 
                        'Use_Case': ', '.join, 
                        'Revenue':'first' }).reset_index()

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
## TRANSPOSING
df.T

#--------------------------------------------------------
## JOINS
# http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#compare-with-sql-join
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html
    #default is inner join
    #can also use left_on=, right_on=
df=pd.merge(df1, df2, on='Country')
df = pd.merge(df1, df2, how='left', left_on=['id_key'], right_on=['fk_key']) #if join fields are different
df = pd.merge(df1, df2, how='left', left_on=['id_key','field2','field3'], right_on=['fk_key','field2','field3']) #multiple join fields
hudf=pd.merge(hdf, ul, how ='left', on=['State','RegionName']) #join on multiple columns
    #indicator give an additional field '_merge'.
    # Can use groupby size to count number of left-only, right-only, or both
df=pd.merge(df1, df2, how='outer', on='Country', indicator=True)
df.groupby('_merge').size()


    #join by index
df=pd.concat([df1,df2], axis=1, join_axes=[df1.index])
df=pd.concat([df1,df2], axis=1) #or if they are already sorted properly


## UNION
df1=pd.read_csv('Redemption_Part1.csv')
df2=pd.read_csv('Redemption_Part2.csv')
df3=pd.read_csv('Redemption_Part3.csv')
frames=[df1,df2,df3]
df_new = pd.concat(frames)


## APPEND
df = df.append(df2, ignore_index=True)


#--------------------------------------------------------
## ENCODE CATEGORICAL TO INTEGERS

df2['Gene'] = df2['Gene'].astype('category') # first change an object to category
df2['code'] = df2['Gene'].cat.codes     # then extract their code out
# when training a model, can just use ".cat.codes" to fit the model


#--------------------------------------------------------
## DATES
    #change string to date format
col = pd.to_datetime(df.columns[6:])
col = pd.to_datetime(df['date'],dayfirst=True)  #sometimes the auto-format is wrong, and you need specify dayfirst or yearfirst
    #aggregation by date intervals
    #list of rules can be found in url: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
    #date must be in index, while the dataframe contains only the col you want to aggregate
date=date.resample('Q').mean()  #by quarter, also (Day: D, Week: W, Month: M, Quarter: Q, Year: Y)
                 
    #change date to string
date_yr=a['column_nm'].dt.strftime('%Y') #change to year

    #change to hour
df['hour'] = df['Time'].apply(lambda x: x.hour)
    #change to day of week
df['day_of_week'] = df['my_dates'].dt.weekday_name
    #set constant for date, minute, second
df2['hour'] = pd.to_datetime('1900-01-01') + pd.to_timedelta(df3['Time'].dt.hour, unit='H')

    # from epoch, i.e., seconds since 1970
    # check datetime format: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
dfr['event_ts']=  dfr['Event-Timestamp'].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)))
dfr['event_ts']= pd.to_datetime(dfr['Event-Timestamp'], unit='s', errors='coerce') #note that this STILL needs to convert to local time


#--------------------------------------------------------
## Split commas in cells and stack them in new rows
    # https://stackoverflow.com/questions/17116814/pandas-how-do-i-split-text-in-a-column-into-multiple-rows
    
# 1) isolate column with comma, split them, and stack them as single rows
p = df['producer'].str.split(', ').apply(pd.Series, 1).stack()
# 2) remove multi dimensions index
p.index = p.index.droplevel(-1)
# 3) add series must have a name
p.name = 'producer'
# 4) use inner join to add based on index value
df.join(p)