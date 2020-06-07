### Easiest
Install Anaconda, comes with most of the important packages.

### Check version in command line
python -V

### install packages using wheel
   * Important for computers without internet access.
   * Unofficial but convenient wheel files to download from https://www.lfd.uci.edu/~gohlke/pythonlibs/

### install using pip
  * ``pip install packageName``: Install package
  * ``pip install --upgrade packageName``: Upgrade package version
  * ``pip install -r requirements.txt``: install from requirements.txt
  * ``pip freeze``: Print list of packages installed
  * ``pip uninstall packageName``: Uninstall package
  * ``pip show packageName``: show package version, license, filepath etc.

### Check paths of all python installations
  * windows cmd: `where python`
  * Bash: `which python`

### Site Packages
Mac/Ubuntu:
  * /anaconda3/lib/python3.7/site-packages
  * OR in python shell
```from distutils.sysconfig import get_python_lib
print(get_python_lib())
```


### Change Default Python Path

in windows:
  
  * Go control panel > System & Security > System > Advanced system settings > Environment Variables > System variables
  * Search and click on PATHS
  * Python paths are indicated here. Those that are in front will be the default. Just cut and paste them to after the python version you want to be the first
  * Some important paths to add in
      - ``C:\Users\xxxx\Anaconda3``: must have 
      - ``C:\Users\xxxx\Anaconda3\Scripts``: need this to have access to pip
  * Note that these two paths have to stick together, else you might be using another version of python to pip install packages
  
in mac:

  * ``open -a TextEdit .bash_profile``: open this file. All installed python paths are here. Just cut and paste the one that needs to be the default to the bottom. Save and close.
  * ``source ~/.bash_profile`` reload the bash profile and use ``python --version`` to check if the changes are made.
  
in VSCode:

 * terminal in VSCode might be by default python 2.7. If you have anaconda python 3+ installed, just type ``conda`` and it should convert to anaconda python path.


### Import Relative Path of Local Packages
```
import sys, os
sys.path.append('../')
import package_name
```


### Creating Requirements.txt

 * ``pip install pipreqs``
 * ``pipreqs .``: make a requirement.txt file in current directory with all imported packages
 * ``pipreqs . --force``: overwrite existing requirements.txt