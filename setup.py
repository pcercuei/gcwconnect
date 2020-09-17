#!/usr/bin/env python3

from setuptools import setup

setup(
        name = 'gcwconnect',
        description = 'OpenDingux wireless configuration tool',
        py_modules=['gcwconnect'],
        url='https://github.com/skipmeister123/gcwconnect',
        packages = ['data'],
        package_data = { 'data': ['*.png', 'gcwzero.ttf', 'Inconsolata.otf'], },
)
