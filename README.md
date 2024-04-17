<img src="https://raw.githubusercontent.com/battleoverflow/faye/main/assets/faye.jpg" />

Basic logging library with a customizable log message and progress bar!

The best way to utilize the Faye library is by installing via `pip`. You can install the library by running the following command:
```bash
pip install faye
```

## Usage
The library is currently limited due to it being updated on a necessity basis, but there are a few examples below to help with using it.

```python
# Import the Faye library
from faye import Faye

# Prints a "CRITICAL" log message to stdout
print(Faye.log(msg="Faye is awesome!", level="CRITICAL"))

# You can also use integer values for the level
print(Faye.log(msg="Faye is awesome!", level=5))

# Currently supported levels:
# - TRACE (0)
# - DEBUG (1)
# - INFO (2)
# - WARNING (3)
# - ERROR (4)
# - CRITICAL (5)

# You can add a splash of color to the logging as well
print(Faye.log(msg="Faye is awesome!", level="CRITICAL", color=True))

# Prints a basic progress bar to stdout
print(Faye.progress(total=100, description="Downloading..."))
```
