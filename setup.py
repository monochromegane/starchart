#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='starchart',
    version='0.0.2',
    description='StarChart is a tool to manage Google Cloud Machine Learning training programs and model versions.',
    author='monochromegane',
    url='https://github.com/monochromegane/starchart',
    packages=find_packages(),
    install_requires=['google-cloud-storage', 'google-api-python-client'],
    entry_points={
        'console_scripts': 'starchart=starchart.main:main'
    }
)
