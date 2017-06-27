## Using Sphinx
  * In cmd or terminal > `sphinx-quickstart`
  * master document is the home page
  * `make html` OR `./make html` (in atom powershell) command to create html document, note to cd to folder where rst file is stored
  * Html pages stored under `_build/html` folder

## Themes
  * Built in themes: `alabaster` (default), `classic`, `sphinxdoc`, `scrolls`, `agogo`, `traditional`, `nature`, `haiku`, `pyramid`, `bizstyle`
  * Nicest theme is provided by readthedocs.org. View here on how to install https://pypi.python.org/pypi/sphinx_rtd_theme
  * `pip install sphinx_rtd_theme`
  * Add config.py with

``` 
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```
## Auto Docstrings
  * A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition
  * Ensure the docstrings are formatted correctly
  * Set `y` to set autodoc at `sphinx-quickstart` stage
  * At conf.py uncomment the following
  
```
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
```

  * Change abspath if python code is in different directory
  * In rst file, set python file name without extension

```
.. automodule:: filename
    :members:
```

## Sidebar
```
.. sidebar:: title
 
    *Paragraph 1*. Statement 1.
 
    *Paragraph 2*. Statement 2.
```

## Table of Contents
  * Define max depth to display based on headers === & ----
  * Add in additional pages (.rst files) using the file name
  * Add auto-numbering if necessary
  
```
.. toctree::
   :maxdepth: 1
   :caption: Contents
   :numbered:
  
   page 1
   page 2
```

## Other Commands
  * __Code__: enclosed in backticks ``
  * __Bold__: enclosed in asterieks **
  * __Hyperlink__: enclosed in backticks \`PyPI <https://pypi.python.org/pypi/Sphinx>\`

## Resources
  * __Sphinx Documentation__: http://www.sphinx-doc.org/en/stable/index.html
  * __Cheatsheet Matplotlib__: http://matplotlib.org/sampledoc/cheatsheet.html
  * __Themes__: http://www.writethedocs.org/guide/tools/sphinx-themes/
  * __Docstrings__: https://www.python.org/dev/peps/pep-0257/
  * __Autodoc__: https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/