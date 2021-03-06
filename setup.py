#!/usr/bin/env python

from setuptools import setup

setup(
    # Application name:
    name='download_espa_order',

    # Version number:
    version='1.0.0',

    # Application author details:
    author='David V. Hill',

    license=open('LICENSE.txt').read(),

    description='Client for downloading ESPA scenes.',
    long_description=open('README.md').read(),

    classifiers = [
        'Programming Language :: Python',
        'Programming Langauge :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: GIS'
    ],

    # Scripts
    # Moves the script to the user's bin directory so that it can be executed.
    # Usage is 'download_espa_order.py' not 'python download_espa_order.py'
    scripts=['download_espa_order.py'],

    # Dependent packages (distributions)
    install_requires=[
        'feedparser <= 5.1.2, >=5.1.2'
    ],
)
