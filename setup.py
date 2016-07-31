import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "corenlp_pywrap",
    version = "0.0.6",
    author = "hhsecond",
    author_email = "sherinct@live.com",
    description = ("A powerful python wraper for Stanford CoreNLP"),
    license = "MIT",
    keywords = "stanford corenlp wrapper",
    install_requires=['requests'],
    url = "https://www.github.com/hhsecond/corenlp_pywrap",
    packages=['corenlp_pywrap'],
    long_description='this is a long description',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
    ],
)