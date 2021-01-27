# Code-Standards

## Black

### Description

Black **auto-formats** python files to adhere to PEP8 format as well as other styles that the team felt is useful. This includes removing whitespaces, new lines, change single to double quotes, and etc.

### Usage

 * Installation: `pip install black`
 * Format Files
    * Single File: `black my_file.py`
    * Directory: `black directory_name`
 * Check Changes w/o Formating
    * `black --diff my_file.py`

---

## Isort

### Description

Sorts by alphabetical order the imported libraries, while splitting python base libraries as first order, with the 3rd party libraries as second order, and local scripts as the third (This can be reconfigured). However, it does not work well for the latter, when you need to add in the sys path before importing local scripts. The sys path will be pushed to the end.

### Usage

 * Installation: `pip install isort`
 * Single File: `isort your_file.py`
 * Directory: `isort your_project/`
 * Check Changes w/o Formating
   * `isort mypythonfile.py --diff`

---

## Flake8

### Description

A wrapper of 3 libraries that **checks (but does not change)**, against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”) and to check cyclomatic complexity.

E***/W***: pep8 errors and warnings
F***: PyFlakes codes (see below)
C9**: McCabe complexity plugin mccabe
N8**: Naming Conventions plugin pep8-naming

### Usage

 * Installation: `pip install flake8`
 * Current Project: `flake8`
 * Single File (and all imported scripts): `flake8 my_file.py`

---

## Darglint

### Description

Checking docstrings.

### Usage

 * Installation: `pip install darglint`
 * Single File: `darglint -v 2 utils_flask2.py`


---

## Bandit

### Description

Tool to find and list common security issues in Python code, with ratings of low, medium and high, as well as description of each vulnerabilities.

### Usage

 * Installation: `pip install bandit`
 * Single File: `bandit your_file.py`
 * Directory: `bandit -r ~/your_repos/project`
 * Display only High Severities: `bandit -r ~/your_repos/project -lll`
 * Json Output: `bandit --format json --recursive project/ -l --output bandit.json`
 * Skip Certain Vulnerabilities, by placing `.bandit` file at directory to check

```
[bandit]
skips: B104,B101
```

---

## Detect Secrets

 * Installation: `pip install detect-secrets`
 * Directory: `detect-secrets scan directory/*`

---

## Safety

### Description

Check vulnerabilities in python libraries.

### Usage

 * Installation: `pip install safety`
 * Check installed packages in VM: `safety check`
 * Check requirements.txt, does not include dependencies: `safety check -r requirements.txt`
 * Full Report: `safety check --full-report`
 * Output: `safety check --json --output insecure_report.json`

---

## Pre-Commit

### Description

Pre-commit is a git hook that you preconfig to run certain scripts, in this case, the above ones before committing to git. A useful compilation is done by https://www.laac.dev/blog/automating-convention-linting-formatting-python/.

 * Installation: `pip install pre-commit`
 * create config file at root of project: `.pre-commit-config.yaml`
   * sample file below
 * Installation (into git hook): `pre-commit install`
 * Uninstallation (from git hook): `pre-commit uninstall`
 * Add Files for Commit: `git add files.py`
 * Run Commit, and Precommit will autorun: `git commit -m 'something'`
 * Skip Hook: `SKIP=flake8 git commit -m "something"`

```yml
default_language_version:
  python: python3
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.3
    hooks:
      - id: flake8
  - repo: https://github.com/PyCQA/bandit
    rev: 1.6.2
    hooks:
      - id: bandit
  - repo: https://github.com/timothycrosley/isort
    rev: 4.3.21
    hooks:
      - id: isort
```