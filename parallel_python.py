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
