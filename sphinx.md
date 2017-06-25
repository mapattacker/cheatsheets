## Introduction to Sphinx
  * In cmd or terminal > `sphinx-quickstart`
  * master document is the home page
  * `make html` OR `./make html` (in atom powershell) command to create html document, note to cd to folder where rst file is stored
  * Html pages stored under `_build/html` folder

## Themes
  * Nicest theme is provided by readthedocs.org. View here on how to install https://pypi.python.org/pypi/sphinx_rtd_theme
  * pip install sphinx_rtd_theme
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

## Resources
  * __Sphinx Documentation__: http://www.sphinx-doc.org/en/stable/index.html
  * __Themes__: http://www.writethedocs.org/guide/tools/sphinx-themes/
  * __Docstrings__: https://www.python.org/dev/peps/pep-0257/
  * __Autodoc__: https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/