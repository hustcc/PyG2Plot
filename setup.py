# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree
from setuptools import Command, find_packages, setup


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

__requires__ = ["jinja2~=2.11.2", "simplejson"]
__extra_requires__ = {
}

__keywords__ = ["AntV", "G2Plot", "charts", "PyG2Plot", "visualization"]

# Load the package's _version.py module as a dictionary.
here = os.path.abspath(os.path.dirname(__file__))
meta = {}
with open(os.path.join(here, __title__, "meta.py")) as f:
    exec(f.read(), meta)

__version__ = meta["__version__"]
__author__ = meta["__author__"]


class UploadCommand(Command):
    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        print("✨✨ {0}".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
            rmtree(os.path.join(here, "build"))
            rmtree(os.path.join(here, "{0}.egg-info".format(__title__)))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution…")
        os.system("{0} setup.py bdist_wheel".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
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
    cmdclass={"upload": UploadCommand},
    extras_require=__extra_requires__,
)
