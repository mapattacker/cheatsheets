
## TLDR

 * cd to folder > `pytest` or `pytest -v`

## PYTEST.INI

Create an ini file `touch pytest.ini` for customisation.

```
[pytest]
python_files = test_*
python_classes = *_Tests
python_functions = test_*
```