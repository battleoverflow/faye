<h1 align="center">
    <img src="https://raw.githubusercontent.com/shinigamilib/faye/main/.github/assets/faye_logo.jpg" />
    <br />
    Faye
</h1>

Basic logging library created for any Python project with little overhead, an awesome progress bar, and customizable logging!

This project was created as a logging library for [Shinigami](https://github.com/shinigamilib/shinigami-py), but is compatible with almost any project using Python 3.

Faye can also be installed using pip!
```bash
pip install faye
```

## Example
```python
from faye.faye import Faye

# Logging
print(Faye.log(msg="Faye is awesome", level="CRITICAL"))

# Progress Bar
print(Faye.progress(total=100, description="Downloading..."))
```