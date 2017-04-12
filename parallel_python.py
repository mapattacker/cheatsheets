#pip install feather-format
#for reading and writing binary data frames fast


# check no. of cores
import multiprocessing
print multiprocessing.cpu_count()


# use multiprocessing pool
# https://www.youtube.com/watch?v=s1SkCYMnfbY
#------------------------------

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
    pool = mp.Pool(processes=4, maxtasksperchild=1)
    # separate the list of files such that only 1 file take one core (chunksize)
    pool.map(unziptar, my_files, chunksize=1)
    pool.close()

# need this "if" else windows will have recursive error
if __name__ == "__main__":
    start = time()
    path = r"/Users/siyang/Desktop/test"
    fanout_unziptar(path)
    end = time()
    print 'script ended after {} mins'.format((end-start)/60)

# --------------------------------
# EXAMPLE 2

