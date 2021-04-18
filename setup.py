#!/usr/bin/env python

import os
import re
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup  # type: ignore

# Package meta-data
NAME = "best-of"
MAIN_PACKAGE = "best_of"  # Change if main package != NAME
DESCRIPTION = "Generates a ranked list of awesome libraries and tools."
URL = "https://github.com/best-of-lists/best-of-generator"
EMAIL = "best-of@mltooling.org"
AUTHOR = "Best-of Team"
LICENSE = "GPLv3"
REQUIRES_PYTHON = ">=3.6"
VERSION = None  # Only set version if you like to overwrite the version in _about.py

PWD = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with open(os.path.join(PWD, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Extract the version from the _about.py module.
if not VERSION:
    with open(os.path.join(PWD, "src", MAIN_PACKAGE, "_about.py")) as f:  # type: ignore
        VERSION = re.findall(r"__version__\s*=\s*\"(.+)\"", f.read())[0]

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license=LICENSE,
    packages=find_packages(where="src", exclude=("tests", "test", "examples", "docs")),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    zip_safe=False,
    install_requires=[
        "pandas",
        "numpy",
        "click",
        "tqdm",
        "pybraries",
        "requirements-parser",
        "pypistats",
        "requests",
        "addict",
        "beautifulsoup4",
        "PyYAML",
        "python-dateutil",
        "pyppeteer",
    ],
    # deprecated: dependency_links=dependency_links,
    extras_require={
        # extras can be installed via: pip install package[dev]
        "dev": [
            "setuptools",
            "wheel",
            "twine",
            "flake8",
            "pytest",
            "pytest-mock",
            "pytest-cov",
            "mypy",
            "black",
            "pydocstyle",
            "isort",
            "lazydocs",
        ],
    },
    include_package_data=True,
    package_data={
        # If there are data files included in your packages that need to be
        # 'sample': ['package_data.dat'],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console",
    ],
    project_urls={
        "Changelog": URL + "/releases",
        "Issue Tracker": URL + "/issues",
        "Documentation": URL + "#documentation",
        "Source": URL,
    },
    entry_points={"console_scripts": [f"{NAME}={MAIN_PACKAGE}._cli:cli"]},
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
)
