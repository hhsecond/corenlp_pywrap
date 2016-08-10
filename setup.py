import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
setup(
    name = "corenlp_pywrap",
    version = "1.0.0",
    author = "hhsecond",
    author_email = "sherinct@live.com",
    description = ("A powerful python wraper for Stanford CoreNLP"),
    license = "MIT",
    keywords = "stanford corenlp wrapper",
    install_requires=['requests'],
    url = "https://www.github.com/hhsecond/corenlp_pywrap",
    download_url = "https://www.github.com/hhsecond/corenlp_pywrap/tarball/1.0.0",
    packages=['corenlp_pywrap'],
    long_description='Production Ready version equiped with basic'\
        'output fetch of stanfornlp and custom arrange function, '\
        'for more Info - '\
        'CheckItOut: https://github.com/hhsecond/corenlp_pywrap',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
    ],
)