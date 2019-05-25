#--------------------------------------------------------
# READ WRITE

# csv
df <- read.csv('/Users/xx/Desktop/Book1.csv')
write.csv(df, file='/Users/xx/Desktop/Book1.csv')

# excel
library(readxl)
df <- read_excel('/Users/Siyang/Desktop/Book1.xlsx', sheet='Sheet1')
df <- read_excel('/Users/Siyang/Desktop/Book1.xlsx', sheet=1) # indicate sheet no.
library(xlsx)
write.xlsx(df, "Book1.xlsx")



#--------------------------------------------------------
# SAMPLE DATASETS

data() #shows list of sample datasets
state.x77
iris



#--------------------------------------------------------
# BASICS 
class(df) #"data.frame"
summary(df)
str(df)

dim(df) #shape
nrow(df) #rows
ncol(df) #columns

colnames(df)




#--------------------------------------------------------
# CREATE NEW DATAFRAME
df <- data.frame(col1, col2, col3)



#--------------------------------------------------------
# INDEXING
head(df)

# rows start:end, column_names
df[1:5,] #select first 5 rows
df[,1:2] #select first 2 columns

df[[2,'colname']] #output cell value
df[[2,'colname']] <- 5 #change cell value to 5

# select features
df$name #array
df['Sepal.Length'] #dataframe


#--------------------------------------------------------
# FILTER
subset(df, subset= col1==True)
subset(df, subset=Sepal.Length>7)