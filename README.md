<h1 align="center">
    <img src=".github/assets/faye_logo.jpg" />
    <br />
    Faye
</h1>

Basic logging library created for any Python project with little overhead, an awesome progress bar, and customizable logging!

This project was created as a logging necessesity for [Shinigami](https://github.com/stience/shinigami), but is compatible with almost any project.

Faye can also be installed using pip!
```bash
pip3 install faye
```

## Example
```python
from faye.faye import Faye

# Logging
print(Faye.log(msg="Faye is awesome", level="CRITICAL"))

# Progress Bar
print(Faye.progress(total=100, description="Downloading..."))
```