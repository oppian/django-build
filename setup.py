'''
Created on 5 Mar 2010

@author: oppianmatt
'''

# hook to find setup tools if not installed
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "django-build",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['boto'],
    
    # metadata for upload to PyPI
    author = "Oppian",
    author_email = "matt@oppian.com",
    description = "django-build provides a management command 'build2s3' which tar and gzips the source code and stores it in s3.",
    license = "MIT",
    keywords = "django s3 build",
    url = "http://oppian.com/labs/django-build/",   # project home page, if any
)

