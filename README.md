<img src="https://raw.githubusercontent.com/shinigamilib/faye/main/assets/faye.jpg" />

Basic logging library with a customizable log message, progress bar, and more!

This logging library was created specifically for [Shinigami (Python)](https://github.com/shinigamilib/shinigami-py), but you should have no issues integrating it into your codebase as long as you're running Python 3.

The best way to utilize the Faye library is by using `pip`. You can install the library by running the following command:
```bash
pip install faye
```

## Usage
The library is currently limited due to it being updated on a necessity basis, but there are a few examples below to help with using it.

```python
# Imports the Faye library
from faye.faye import Faye

# Prints a "CRITICAL" log message to stdout
print(Faye.log(msg="Faye is awesome!", level="CRITICAL"))

# Prints a basic progress bar to stdout
print(Faye.progress(total=100, description="Downloading..."))
```

Even though Faye should be compatible with most Python 3 projects, it is still in an early stage of development. This means Faye could be altered at any time.