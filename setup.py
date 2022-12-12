"""
    Owner: CyberSuki (https://github.com/cybersuki)
    Project: Faye
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "faye",
    version = "0.1.3",
    author = "Hifumi1337",
    description = "Basic logging library created for any Python project with little overhead, an awesome progress bar, and customizable logging!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/cybersuki/faye",
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