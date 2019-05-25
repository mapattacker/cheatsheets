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
head(df)
class(df) #"data.frame"
summary(df)
str(df)

# select features
df$name #array
df['Sepal.Length'] #dataframe



#--------------------------------------------------------
# CREATE NEW DATAFRAME
df <- data.frame(col1, col2, col3)


#--------------------------------------------------------
# LINEAR REGRESSION

model <- lm(y ~ x1, x2, x3, data=df)