#pip install feather-format
#for reading and writing binary data frames fast


# check no. of cores
import multiprocessing
print multiprocessing.cpu_count()


# use multiprocessing pool
#------------------------------
from multiprocessing import Pool
from multiprocessing import cpu_count
import time

start = time.time()
core = cpu_count()

def f(x):
    return x*x

if __name__ == '__main__':
    test = range(80000000)
    pool = Pool(processes=core)
    results = pool.map(f, test)

# test using normal loop
# record = []
# for i in range(8000000):
#     record.append(f(i))

end = time.time()
print end-start
#------------------------------



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


