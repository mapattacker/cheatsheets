## Using Sphinx
  * In cmd or terminal > `sphinx-quickstart`
  * master document is the home page
  * `make html` OR `./make html` (in atom powershell) command to create html document, note to cd to folder where rst file is stored
  * Html pages stored under `_build/html` folder

## Using readthedocs
  * readthedocs: go to new build > Admin > Integrations > Add Integrations > copy weblink created (include https:// in front!!)
  * Github: go to repository > Settings > Webhooks > Add Webhook > paste weblink > content type as "application/x-www-form-urlencoded..." > Secret leave blank > just push event > Update webhook

## Themes
  * Built in themes: `alabaster` (default), `classic`, `sphinxdoc`, `scrolls`, `agogo`, `traditional`, `nature`, `haiku`, `pyramid`, `bizstyle`
  * Nicest theme is provided by readthedocs.org. View here on how to install https://pypi.python.org/pypi/sphinx_rtd_theme
  * `pip install sphinx_rtd_theme`
  * In config.py:
    * Comment out `html_theme = 'alabaster'` and in place of it
    * Add in the codes

```python
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

## Headings
  * header 1 ====
  * header 2 -------
  * header 3 \*\*\*\*\*\*\*
  * header 4 ^^^^^^^


## Lists
  * bullet `*`
  * Numbered list `1.` etc.
  * Nested lists, with indentation after a space

  ```
    1. 1st level bullet

        a. 2nd level bullet
  ```



## Auto Docstrings
  * A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition
  * Ensure the docstrings are formatted correctly
  * Set `y` to set autodoc at `sphinx-quickstart` stage
  * At conf.py uncomment the following

```python
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
```

  * Change abspath if python code is in different directory
  * In rst file, set python file name without extension

```restructuredtext
.. automodule:: filename
    :members:
```

## Sidebar
```restructuredtext
.. sidebar:: title

    *Paragraph 1*. Statement 1.

    *Paragraph 2*. Statement 2.
```

## Table of Contents
  * Define max depth to display based on headers === & ----
  * Add in additional pages (.rst files) using the file name
  * Add auto-numbering if necessary
  * Possible to hide it on main page

```restructuredtext
.. toctree::
   :maxdepth: 2
   :caption: Contents
   :hidden:
   :numbered:

   page 1
   page 2
```

## Tables
  * Use the table generator in the link: http://www.tablesgenerator.com/text_tables


## Paragraph Level Markup
  * Note
  ```restructuredtext
  .. note::

     This function is not suitable for sending spam e-mails.
  ```
  * Warning
  ```restructuredtext
  .. warning::

     An important bit of information about an API.
  ```
  * Error/Danger
  ```restructuredtext
  .. error::
     This is sample of admonition directive for "Error".
  ```
  * Hint/Tip
  ```restructuredtext
  .. tip::
     This is sample of admonition directive for "Tip".
  ```

## Blocks
  * Code Block
  ```restructuredtext
  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    for i in range(1,10):
      print i
  ```
  * Normal block
  ```
  ::

    Some text here.
  ```
  * __Shell Code__: triple arrows with blank new line space give syntax highlighting `>>> print something`. Next line will be a comment out sentence.
  * __Small Red Block__: enclosed in double backticks \`\` \`\`

## Images
  * Image only
  ```restructuredtext
  .. image:: workflow.png
      :scale: 40 %
      :align: left
  ```

  * image with caption

  ```restructuredtext
  .. figure:: images/rankingencode.png
      :width: 200px
      :align: center
      :height: 100px
      :alt: alternate text
      :figclass: align-center

      Write caption here.
  ```

  * image with attachment
  
  ```restructuredtext
  .. image:: images/sklearn.PNG
      :target: _static/sklearn_cheat.pdf
  ```

## Other Commands
  * __Bold__: enclosed in double asterieks ** **
  * __Italics__: enclosed in asterieks * *
  * __Line Break__: pipe |
  * __Undo rst Commands__: \
  * __Images__: `.. image:: workflow.png`
  * __Hyperlink__: assign a variable then call hyperlink below:
  ```restructuredtext
  Document dated Jun 2000. Download_.

  .. _Download: https://tools.ietf.org/html/rfc2865
  ```
  * __SVG images__: put svg file in html/_images folder and use a raw directive to link to it
  ```restructuredtext
  .. raw:: html

      <object data="_images/workflow.svg" type="image/svg+xml"></object>
  ```

## Config File
  * __Remove 'show source file' link__: add this line to conf.py `html_show_sourcelink = False`


## Generating PDF
  * Windows: install texlive. http://www.tug.org/texlive/
  * Mac: `sudo apt-get install wget build-essential python2.7-dev texlive-full`
  * Build latex files `make latex`
  * Go to latex folder `cd _build/latex`
  * Create pdf document by selecting the .tex document `pdflatex filename.tex`
  * PDF will be created in the same folder


## Resources
  * __Sphinx Documentation__: http://www.sphinx-doc.org/en/stable/index.html
  * __Sphinx Memo__: http://rest-sphinx-memo.readthedocs.io
  * __Cheatsheet Matplotlib__: http://matplotlib.org/sampledoc/cheatsheet.html
  * __Cheatsheet Ralsina__: https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
  * __Themes__: http://www.writethedocs.org/guide/tools/sphinx-themes/
  * __Docstrings__: https://www.python.org/dev/peps/pep-0257/
  * __Autodoc__: https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/
