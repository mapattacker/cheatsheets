# remove error msg in a cell, MUST be at first line
%%capture --no-stdout --no-display


# display html
from IPython.core.display import display, HTML
html = 'https://github.com/PAIR-code/facets/blob/master/facets_dive/Dive_demo.ipynb'
display(HTML(html), width=400)


#--------------------------------------------------------
# jupyter notebook magic functions
%lsmagic #list all magic
%%timeit -n 100 #time script to complete, -n 100 means only loop 100 times; default is 100
%%time #time just once with CPU time outputs
%%bash #run bash commands in mac
%%cmd #run command prompt in windows


#--------------------------------------------------------
# Table of Contents
# Collapsible Headers
# https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
conda install -c conda-forge jupyter_contrib_nbextensions


#--------------------------------------------------------
from IPython.display import Audio
Audio('data/nightingale.wav')


# Anchor Links #---------------------------

# Table of Contents
 * <a href="#1">Import Packages</a>
 * <a href="#2">Functions</a>
 * <a href="#3">Fault Detection</a>
   * <a href="#3.1"><b>Test Case 1</b>: Common Features</a>
   * <a href="#3.2"><b>Test Case 2</b>: Less Features</a>
 * <a href="#4">Severity Detection</a>
   * <a href="#4.1"><b>Test Case 3</b>: Common Features</a>
   * <a href="#4.2"><b>Test Case 4</b>: Important Features</a>
 * <a href="#5">Query Strategies</a>
 * <a href="#6">Conclusion</a>


<a id='1'></a>
# Import Packages
