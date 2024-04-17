"""
    Project: Faye (https://github.com/battleoverflow/faye)
    Author: battleoverflow (https://github.com/battleoverflow)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "faye",
    version = "0.1.11",
    author = "battleoverflow",
    description = "Basic logging library with a customizable log message and progress bar!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/battleoverflow/faye",
    py_modules=["shinigami"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6"
)
