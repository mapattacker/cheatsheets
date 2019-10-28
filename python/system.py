import sys

# import own modules from different folders
    # normally, we can only import from python site-package directory, or modules in current directory
    # we can insert a new system path so that python can register that directory
sys.path.insert(0, '../folder_name')
import module_name