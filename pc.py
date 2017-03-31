
# get list of selected file names in current directory
import glob
for i in glob.iglob('*eapsim*'):
  print i
  

# get current directory name
import os
directoryName = os.path.relpath(".","..")


# get all files & folders in path listed (as a list)
import os
# Open a file
path = 'C:\Users\Teo Siyang\Dropbox\wifi'
for i in os.listdir( path ):
  print i

    
# get full path, folder name (in a list), and file names (in a list) from path lsited
import os
path = 'C:\Users\Teo Siyang\Dropbox\wifi'
for root, dirs, files in os.walk(path):
    print root, dirs, files

    
# http://en.cppreference.com/w/cpp/io/c/fopen
# File access mode string | Meaning | Explanation | Action if file already exists | Action if file does not exist
# "r"	read | Open a file for reading | read from start | failure to open
# "w"	write | Create a file for writing | destroy contents | create new
# "a"	append | Append to a file | write to end | create new
# "r+"	read extended | Open a file for read/write | read from start error
# "w+"	write extended | Create a file for read/write | destroy contents | create new
# "a+"	append extended | Open a file for read/write | write to end | create new
