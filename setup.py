"""
    Owner: Azazel Software
    Learn more: https://github.com/AzazelSoftware
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "faye",
    version = "0.1.6",
    author = "Azazel Software",
    description = "Basic logging library with a customizable log message, progress bar, and more!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/AzazelSoftware/faye",
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