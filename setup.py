# -*- coding: utf-8 -*-
import io
import os
from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

# RELEASE STEPS
# $ python setup.py upload


__title__ = "pyg2plot"
__description__ = "Python3 binding for `@AntV/G2Plot` Plotting Library, make charting easier."
__long_description__ = read('README.md')
__url__ = "https://github.com/hustcc/pyg2plot"
__author_email__ = "i@hust.cc"
__license__ = "MIT"

__requires__ = ["jinja2~=2.11.2"]
__extra_requires__ = {
}

__keywords__ = ["AntV", "G2Plot" "charts", "visualazation"]

# Load the package's _version.py module as a dictionary.
here = os.path.abspath(os.path.dirname(__file__))
meta = {}
with open(os.path.join(here, __title__, "meta.py")) as f:
    exec(f.read(), meta)

__version__ = meta["__version__"]
__author__ = meta["__author__"]

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    packages=find_packages(exclude=("tests",)),
    keywords=__keywords__,
    install_requires=__requires__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
    extras_require=__extra_requires__,
)
