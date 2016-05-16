"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from setuptools import Command, find_packages, setup
from lib import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'pymy',
    version = __version__,
    description = 'Command line tool for migrating mysql table data between databases',
    long_description = long_description,
    url = 'https://github.com/juwilliams/pymy',
    author = 'Justin Williams',
    author_email = 'justin.williams@rpdmsolutions.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: mysql database users',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs']),
    install_requires = ['docopt'],
    entry_points = {
        'console_scripts': [
            'pymy=lib.cli:main',
        ],
    },
)