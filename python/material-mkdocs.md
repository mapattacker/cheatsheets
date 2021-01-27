# Material for Mkdocs

A documentation theme that is both easy to use and beautiful. Best to use this
over the old Sphinx themes.

## Installation

```bash
pip install mkdocs-material
```

## Setting Up

* Go to repo root directory
    * create a `mkdocs.yml` file
    * use the following template as a start

```yml
site_name: Python Computer Vision
theme:
    name: 'material'
    palette:
        primary: 'black'

nav:
    - Introduction: index.md
    - Image Basics: basics.md

repo_name: mapattacker/computer-vision-python
repo_url: https://github.com/mapattacker/computer-vision-python

markdown_extensions:
    - codehilite
```

* Create a ``docs`` folder
    * store all your markdown `.md` documentations here

* Use `mkdocs gh-deploy` to generate the html and other web related files
    * this creates a new branch called gh-pages, and put all html files here
* Settings > Github Pages > Source > change to gh-pages
* Upload all files and changes to the remote git repository
* The documentation site will be available at ``https://{username}.github.io/{repo-name}/``