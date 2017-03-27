
# get list of selected file names in current directory
import glob
for i in glob.iglob('*eapsim*'):
  print i
  
# get current directory name
import os
directoryName = os.path.relpath(".","..")
