<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/rmdir.svg?maxAge=3600)](https://pypi.org/project/rmdir/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/rmdir.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/rmdir.py/actions)

### Installation
```bash
$ [sudo] pip install rmdir
```

#### Examples
```bash
$ find . -depth -type d -exec rmdir {} \; 2>/dev/null
```

```python
>>> import rmdir
>>> rmdir.rmdir(".")
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>