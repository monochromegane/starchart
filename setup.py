#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='starchart',
    author='monochromegane',
    packages=find_packages(),
    install_requires=['google-cloud-storage'],
    entry_points={
        'console_scripts': 'starchart=starchart.main:main'
    }
)
