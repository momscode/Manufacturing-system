# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in manufacturing_system/__init__.py
from manufacturing_system import __version__ as version

setup(
	name='manufacturing_system',
	version=version,
	description='Custom Application For Electrical Manufacturing',
	author='Momscode technologies',
	author_email='info@momscode.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
