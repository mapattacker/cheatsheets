### Easiest
Install Anaconda, comes with most of the important packages.

### install packages using wheel
   * Important for computers without internet access.
   * 

### install using pip
  * ``pip install packageName``: Install package
  * ``pip install --upgrade packageName``: Upgrade package version
  * ``pip freeze``: Print list of packages installed
  * ``pip uninstall packageName``: Uninstall package

  
### Change default python path

in windows:
  
  * Go control panel > System & Security > System > Advanced system settings > Environment Variables > System variables
  * Search and click on PATHS
  * Python paths are indicated here. Those that are in front will be the default. Just cut and paste them to after the python version you want to be the first
  
in mac:

  * ``open -a TextEdit .bash_profile``: open this file. All installed python paths are here. Just cut and paste the one that needs to be the default to the bottom. Save and close.