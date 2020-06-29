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
import multiprocessing as mp

def worker(files):
    some task
    
def pooling(allfiles, name, newfolderpath, acctHeader, fieldnamefile):
    list_to_iterate = [file1, file2, file3, file4]

    process_spawn = min(mp.cpu_count(), len(allfiles)) 
    pool = mp.Pool(process_spawn)
    pool.map(worker, list_to_iterate, chunksize=1)
    pool.close()


#---------------------------------------
# for worker function that require more than one variable, use 'partial' function to 'group' them together
import multiprocessing as mp
from functools import partial

def fdtw(match, pattern, features, distances):
    do_something

def pooling(win_slices, pattern, features, cores=1):
    processes = round(min(mp.cpu_count(), len(win_slices))*cores)
    pool = mp.Pool(processes)
    fdtw_partial = partial(fdtw, pattern=pattern, features=features, distances=distances)
    pool.map(fdtw_partial, win_slices, chunksize=1)
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


# set special list for results of multiprocess to pump within
distances = mp.Manager().list()


# set error logging
import logging
mpl = mp.log_to_stderr()
mpl.setLevel(logging.INFO)





# execute different functions concurrently -----
# v1
from functools import partial
from multiprocessing import Pool


def a(param1, param2, param3):
    return param1 + param2 + param3


def b(param1, param2):
    return param1 + param2


def smap(f):
    return f()


func1 = partial(a, 1, 2, 3)
func2 = partial(b, 1, 2)

pool = Pool(processes=2)
res = pool.map(smap, [func1, func2])
pool.close()
pool.join()
print(res)



# v2
from multiprocessing import Process
import os
import datetime


def func_1(title):
    now = datetime.datetime.now()
    print "hello, world"
    print "Current second: %d" % now.second
    print "Current microsecond: %d" % now.microsecond


def func_2(name):
    now = datetime.datetime.now()
    print "Bye, world"
    print "Current second: %d" % now.second
    print "Current microsecond: %d" % now.microsecond


if __name__ == '__main__':
    procs = []
    procs.append(Process(target=func_2, args=('bob',)))
    procs.append(Process(target=func_1, args=('sir',)))
    map(lambda x: x.start(), procs)
    map(lambda x: x.join(), procs)



# MULTI THREADING

from threading import Thread

def do_something(json_input):
    something = json_input
    return something

thread = Thread(target=do_something, kwargs={'json_input': request.args.get('value', json_input)})
thread.start()


# RAY
#---------------------------------------
# use apache arrow backend, supposed much faster then multiprocessing
# https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1



# execute embarassingly parallel task -----
import ray
ray.init()

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))



# execute different functions concurrently -----
import ray

ray.init(num_cpus=2)

# Define functions you want to execute in parallel using 
# the ray.remote decorator.
@ray.remote
def func1():
    print("Working1")

@ray.remote
def func2():
    print("Working2")

# Execute func1 and func2 in parallel.
for i in range(20):
    ray.get([func1.remote(), func2.remote()])