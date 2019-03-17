<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/rmdir.svg?longCache=True)](https://pypi.org/project/rmdir/)
[![](https://img.shields.io/pypi/v/rmdir.svg?maxAge=3600)](https://pypi.org/project/rmdir/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/rmdir.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/rmdir.py/)

#### Installation
```bash
$ [sudo] pip install rmdir
```

#### Functions
function|`__doc__`
-|-
`rmdir.rmdir(path)` |recursively delete empty directories

#### Examples
```bash
$ find . -depth -type d -exec rmdir {} \; 2>/dev/null
```

```python
>>> import rmdir
>>> rmdir.rmdir(".")
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>