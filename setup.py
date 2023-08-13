"""
    Project: Faye (https://github.com/azazelm3dj3d/faye)
    Author: azazelm3dj3d (https://github.com/azazelm3dj3d)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "faye",
    version = "0.1.10",
    author = "azazelm3dj3d",
    description = "Basic logging library with a customizable log message and progress bar!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/azazelm3dj3d/faye",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    packages = [
        "faye"
    ],
    python_requires = ">=3.6"
)