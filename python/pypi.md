# Publishing to PyPi

## Install
 * setuptools
 * twine

## Files Required
 * setup.py
 * MANIFEST.in
 * README.md
 * LICENSE
 * __init__.py

## Create Release
 * Add version tag, in __init__.py
 * Create release in Repo
 * Following semantic versioning 2.0 convention. E.g.
   * v0.1.1-dev.1
   * v0.1.3

## Publish
 * `python setup.py sdist`
 * Check readme
    * `pip install readme_renderer`
    * `python -m readme_renderer README.rst`
 * `twine check dist/*`
 * `twine upload dist/*`