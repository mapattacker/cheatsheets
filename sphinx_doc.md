See https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/

  * in cmd or terminal > `sphinx-quickstart`
  * master document is the home page
  * `make html` OR `./make html` (in atom powershell) command to create html document, note to cd to folder where rst file is stored
  * html pages stored under `_build/html` folder

## Themes
  * Nicest theme is provided by readthedocs.org. View here on how to install https://pypi.python.org/pypi/sphinx_rtd_theme
  * pip install sphinx_rtd_theme
  * Add config.py with

``` 
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```