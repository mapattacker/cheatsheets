# Parallel processing can be done in single machines or distributed in a cluster
  # There are many packages for both.
  # Single machines include multiprocessing & the default package concurrent.futures which work very similarly
  # Clusters include parallel python and jug
  # More here: https://wiki.python.org/moin/ParallelProcessing


# MULTIPROCESSING
# check no. of cores
#---------------------------------------
import multiprocessing as mp
print(mp.cpu_count())


#---------------------------------------
# for worker function that require more than one variable, use 'partial' function to 'group' them together
import multiprocessing as mp
from functools import partial

def worker(files):
    some task
    
def pooling(allfiles, name, newfolderpath, acctHeader, fieldnamefile):
    list_to_iterate = [file1, file2, file3, file4]

    # func = partial(worker, name, newfolderpath, acctHeader, fieldnamefile)
    process_spawn = min(mp.cpu_count(), len(allfiles)) 
    pool = mp.Pool(process_spawn)
    pool.map(worker, list_to_iterate, chunksize=1)
    pool.close()

    
# use multiprocessing pool
# https://www.youtube.com/watch?v=s1SkCYMnfbY
#---------------------------------------
# EXAMPLE 1
# unzip files from different folders
import tarfile
import gzip
import os
import multiprocessing as mp
from time import time


# worker, task to process, i.e., unzipping
def unziptar(folder):
    """worker unzips one file"""
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        if file.endswith("tar.gz"):
            print('extracting... {}'.format(filepath))
            tar = tarfile.open(filepath, 'r:gz')
            tar.extractall(os.path.dirname(filepath))
            tar.close()

# spawn processes for each loop
def fanout_unziptar(path):
    """create pool to extract all"""
    # collect all paths of tar.gz
    my_files = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith("tar.gz"):
                my_files.append(root)
                # my_files.append(os.path.join(root, i))
    my_files = set(my_files) #remove duplicates

    # set number of workers
    # note, for unzipping its I/O intensive~ so allocating too many cores will burn the RAM and make it even slower.
    pool = mp.Pool(processes=4)
    # separate the list of files such that only 1 file take one core (chunksize)
    pool.map(unziptar, my_files, chunksize=1)
    pool.close()

# need this "if" else windows will have recursive error
# a python entry point for a function
if __name__ == "__main__":
    start = time()
    path = r"/Users/jake/Desktop/test"
    fanout_unziptar(path)
    end = time()
    print('script ended after {} mins'.format((end-start)/60))


# Using pandas ----------------
#  IMPT: does not work when applying on string columns

def some_func(x):
    x = x*29/2
    return x

import swifter
train['new_col'] = train['non_string'].swifter.apply(some_func)


# CONCURRENT FUTURES
#---------------------------------------
# concurrent futures uses threads & processes in the same package, making it convenient to switch
import concurrent.futures

def word_length(word):
    return len(word)
words = ["Hello", "are", "you", "thinking", "of", "becoming", "a", "polar", "bear", "?"]

# THREADS
# Threads are good for situations where you have long-running I/O bound tasks 
# but they aren't so good where you have CPU-bound tasks or you have tasks that will run very quickly.
pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
lengths = pool.map(word_length, words)

# PROCESS
# Processes are best when your task is CPU bound or when your task will take long enough.
pool = concurrent.futures.ProcessPoolExecutor(max_workers=10)
lengths = pool.map(word_length, words)

# put results in a list
lengths = list(lengths)



# FEATHER
#---------------------------------------
# http://blog.cloudera.com/blog/2016/03/feather-a-fast-on-disk-format-for-data-frames-for-r-and-python-powered-by-apache-arrow/
    # very fast read & write dataframe format, uses Apache Arrow
    # used for data interoperability between R & Python, not suitable for long term storage atm
import feather
import pandas as pd
# write feather file
feather.write_dataframe(df, 'test.feather')
# read feather file
df2 = feather.read_dataframe('test.feather')


# DISTRIBUTED PARALLEL PROCESSING
#---------------------------------------
pip install pp

import os, re, requests, pp

url_list = ['http://www.google.com/','http://gizmodo.uol.com.br/',
            'https://github.com/', 'http://br.search.yahoo.com/',
            'http://www.python.org/','http://www.python.org/psf/']
result_dict = {}

# identify machines in cluster
ppservers = ("192.168.25.21", "192.168.25.9") 
# Server Class to dispatch processes to different computers
# 1 is specified such that only 1 process in local machine and the rest is distributed to remote computers
# timeout is extended so that it will not shutdown during latency
job_dispatcher = pp.Server(ncpus=1, ppservers=ppservers, socket_timeout=60000)

def aggregate_results(result):
    print "Computing results in main process PID [%d]" %
    os.getpid()
    message = "PID %d in hostname [%s] the following links were "\
    "found: %s" % (result[2], result[3], result[1])
    result_dict[result[0]] = message

def crawl_task(url):
    html_link_regex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')
    request_data = requests.get(url)
    links = html_link_regex.findall(request_data.text)[:3]
    return (url, links, os.getpid(), os.uname()[1])

for url in url_list:
    # crawl_task is the workers
    # returns of workers is sent to callback, i.e. aggregate results
    job_dispatcher.submit(crawl_task, (url,), modules=('os', 're', 'requests',), callback=aggregate_results)

    
job_dispatcher.wait()
print "\nMain process PID [%d]\n" % os.getpid()
for key, value in result_dict.items():
    print "** For url %s, %s\n" % (key, value)
    job_dispatcher.print_stats()


# DASK
#---------------------------------------
# http://dask.pydata.org/en/latest/index.html
# Dask is a flexible parallel computing library for analytic computing.




# NUMBA
#---------------------------------------
# https://numba.pydata.org
# With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, 
# similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.
# Numba works by generating optimized machine code using the LLVM compiler infrastructure at import time, 
# runtime, or statically (using the included pycc tool).

from numba import jit
from numpy import arange

# jit decorator tells Numba to compile this function.
# The argument types will be inferred by Numba when function is called.
@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result

a = arange(9).reshape(3,3)
print(sum2d(a))