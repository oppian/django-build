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
    version = "0.2",
    packages = [
        'build',
        'build.management',
        'build.management.commands',
    ],
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires = ['boto'],
    
    # metadata for upload to PyPI
    author = "Oppian",
    author_email = "matt@oppian.com",
    description = "django-build provides a management command 'build2s3' which tar and gzips the source code and stores it in s3.",
    license = "MIT",
    keywords = "django s3 build",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    url = "http://oppian.com/labs/django-build/",   # project home page, if any
)

