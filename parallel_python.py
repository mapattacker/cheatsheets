# check no. of cores
import multiprocessing
print multiprocessing.cpu_count()


# https://pythonhosted.org/joblib/parallel.html
# using 

%%timeit -n 10
from math import sqrt
x = [sqrt(i ** 2) for i in range(100000)]

%%timeit -n 10
from joblib import Parallel, delayed
import multiprocessing
from math import sqrt
num_cores = multiprocessing.cpu_count()
x = Parallel(n_jobs=num_cores)(delayed(sqrt)(i ** 2) for i in range(100000))



#------------------
import pandas as pd
import numpy as np
col = ['a','b','c','d','e','f']
df = pd.DataFrame(np.random.randint(1, 99, (100000,6)), columns=col)



#------------------
%time
def p1(x):
    df['g'] = df['a'].apply(lambda x: 999 if x == 1 else x)

def p2(x):
    df['h'] = df['b'].apply(lambda x: 999 if x == 1 else x)

def p3(x):
    df['i'] = df['c'].apply(lambda x: 999 if x == 1 else x)

p1(df)
p2(df)
p3(df)
df.head()


#------------------
%time
from multiprocessing import Pool

def p1(x):
    df['g'] = df['a'].apply(lambda x: 999 if x == 1 else x)
def p2(x):
    df['h'] = df['b'].apply(lambda x: 999 if x == 1 else x)
def p3(x):
    df['i'] = df['c'].apply(lambda x: 999 if x == 1 else x)
    
pool = Pool()
result1 = pool.apply_async(p1, [df])    # evaluate "solve1(A)" asynchronously
result2 = pool.apply_async(p2, [df])    # evaluate "solve2(B)" asynchronously
result3 = pool.apply_async(p2, [df])    # evaluate "solve2(B)" asynchronously
answer1 = result1.get()
answer2 = result2.get()

df.head()

#------------------
from multiprocessing import Process

def p1(x):
    df['g'] = df['a'].apply(lambda x: 999 if x == 1 else x)
def p2(x):
    df['h'] = df['b'].apply(lambda x: 999 if x == 1 else x)
def p3(x):
    df['i'] = df['c'].apply(lambda x: 999 if x == 1 else x)
    
p1 = Process(target=p1, args=(df,))
p1.start()
p1.join()

p2 = Process(target=p2, args=(df,))
p2.start()
p2.join()

p3 = Process(target=p3, args=(df,))
p3.start()
p3.join()
