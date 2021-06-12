# Parallel processing can be done in single machines or distributed in a cluster
  # There are many packages for both.
  # Single machines include multiprocessing & the default package concurrent.futures which work very similarly
  # Clusters include parallel python and jug
  # More here: https://wiki.python.org/moin/ParallelProcessing


# More on multiprocessing vs multithreading
  # https://medium.com/towards-artificial-intelligence/the-why-when-and-how-of-using-python-multi-threading-and-multi-processing-afd1b8a8ecca
  # CPU-bound tasks > multiprocessing
      # calculations
  # IO-bound tasks > multithreading
      # network
      # read-write files


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



# set special list or dict for results of multiprocess to pump within
#---------------------------------------
l = mp.Manager().list()

# e.g ----
urls = ["url1", "url2", "url3", "url4"]
def worker(url, l):
    """call individual recommenders & get predictions"""
    data = {"resultSize": "something"}
    prediction = requests.post(url, json=data).content
    prediction = json.loads(prediction)
    l.append(prediction)

def multiproc(urls):
    l = mp.Manager().list()
    worker_ = partial(worker, l=l)
    pool = mp.Pool(4)
    pool.map(worker_, urls, chunksize=1)
    pool.close()
    return l


d = mp.Manager().dict()
# convert dict proxy to dict
d = json.dumps(d.copy())
d = json.loads(d)


# set error logging
import logging
mpl = mp.log_to_stderr()
mpl.setLevel(logging.INFO)


def find_background(img, imgfolder, color="white", threshold="0.3"):
    "worker that that delete images"
    os.remove("some images")
    return img

def find_background_pool(imgfolder, engine, keywords):
    """parallel processing"""
    processes = round(min(mp.cpu_count(), len(img_list_new)))
    pool = mp.Pool(processes)
    find_background_ = partial(find_background, imgfolder=imgfolder, color="white", threshold=0.3)
    # returned images will be all stored within a list
    deleted_imgs = pool.map(find_background_, img_list_new)
    pool.close()



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
# https://stackoverflow.com/questions/48994440/execute-a-function-after-flask-returns-response/51013358
from threading import Thread

def do_something(json_input):
    something = json_input
    return something

thread = Thread(target=do_something, kwargs={'json_input': json})
thread.start()


# https://www.digitalocean.com/community/tutorials/how-to-use-threadpoolexecutor-in-python-3
import requests
import concurrent.futures

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status

wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())


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



# Joblib 
#---------------------------------------

# sequential
sentences = [preprocess(text) for text in pages]
# parallel
from joblib import Parallel, delayed
sentences = Parallel(n_jobs=5)(delayed(preprocess)(text) for text in pages)