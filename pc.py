
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
