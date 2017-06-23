
# check no. of cores
#---------------------------------------
import multiprocessing as mp
print mp.cpu_count()


#---------------------------------------
# for worker function that require more than one variable, use 'partial' function to 'group' them together
import multiprocessing as mp
from functools import partial

def worker(files):
    some task
    
def pooling(allfiles, name, newfolderpath, acctHeader, fieldnamefile):
    func = partial(worker, name, newfolderpath, acctHeader, fieldnamefile)
    pool = mp.Pool(min(mp.cpu_count(), len(allfiles)))
    pool.map(func, allfiles, chunksize=1)
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
            print 'extracting... {}'.format(filepath)
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
    print 'script ended after {} mins'.format((end-start)/60)



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

