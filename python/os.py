# shutdown 
import os
os.system('shutdown -s') # windows
os.system('sudo shutdown now') # linux based

# screenshot
os.system("screencapture screen.png")

# get list of selected file names in current directory
import glob
for i in glob.iglob('*eapsim*'):
    print (i)
  

# get absolute path
import os
os.path.abspath(".")


# get current directory name
import os
directoryName = os.path.relpath(".","..")


# get all files & folders in path listed (as a list)
import os
path = r'C:\Users\Teo Siyang\'
for i in os.listdir(path):
    print (i)


# get full path, folder name (in a list), and file names (in a list) from path listed
import os
path = 'C:\Users\Teo Siyang\'
for root, dirs, files in os.walk(path):
    print (root, dirs, files)
    for i in files:
        print (os.path.join(root,i)) # get full path of files 


# remove a file from directory and all subdirectories
import os
remove_file = '.DS_Store'
path = '/Users/siyang/Desktop/VAMA/scene-understanding'
cnt = 0
for root, dirs, files in os.walk(path):
    for i in files:
        if i == remove_file:
            os.remove(os.path.join(root,i))
            cnt += 1
print('{} files removed'.format(cnt))


# check if a file is present
fieldnamefile = 'filename.txt'
if os.path.isfile(fieldnamefile):
    with open(fieldnamefile, 'rb+') as file: #read field file contents
        for line in file:
            print line
else:
    with open(fieldnamefile, 'ab+') as file: #create new field file
        file.write('headername\n') 

    
# find file dates created or modified time, & file size
import os
import platform
import datetime

path = r'C:\Desktop\foldername'

for root, dir, file in os.walk(path):
    for i in file:
        filenm = os.path.join(root,i)
        # windows
        if platform.system() == 'Windows':
            if i.endswith('csv'): # condition to filter only csv files
                print i, os.path.getctime(filenm)
        else: # linux, mac
            stat = os.stat(filenm)
            try:
                if i.endswith('csv'): 
                    print i, datetime.datetime.fromtimestamp(stat.st_birthtime), stat.st_size
            except AttributeError:
                # No easy way to get creation dates from linux or mac
                # so we'll settle for when its content was last modified.
                if i.endswith('csv'):
                    print i, datetime.datetime.fromtimestamp(stat.st_mtime), stat.st_size

# check file 
os.path.isfile(path) # Boolean

# create directory
newpath = r'C:\Program Files\arbitrary' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

# list files, folders in current directory
os.listdir('.')

# add or remove directory
os.remove() # will remove a file.
os.rmdir() # will remove an empty directory.
shutil.rmtree() # will delete a directory and all its contents.

#  full os path
print os.path.abspath('.') # current directory path
print os.path.abspath('..') # directory 1 level up; every dot brings a level up

#------ FILE HANDLING------------
# http://en.cppreference.com/w/cpp/io/c/fopen
# File access mode string | Meaning | Explanation | Action if file already exists | Action if file does not exist
# "r"	read | Open a file for reading | read from start | failure to open
# "w"	write | Create a file for writing | destroy contents | create new
# "a"	append | Append to a file | write to end | create new
# "r+"	read extended | Open a file for read/write | read from start error
# "w+"	write extended | Create a file for read/write | destroy contents | create new
# "a+"	append extended | Open a file for read/write | write to end | create new

# csv writer
file = open(r'/Users/xxx/Plant Website/website.csv', 'wb')
# quotechar. close the variable in "" if there are any space, quotes etc.
csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
csvwriter.writerow(['genus', 'species', 'author', 'family',\
                    'form', 'status', 'distribution', 'diagnostic',\
                    'references', 'posted_date', 'modified_date', 'url'])

# copying files
from shutil import copyfile
copyfile(file_original, file_new)


# rename file
os.rename('original_name.jpg','new_name.jpg')
