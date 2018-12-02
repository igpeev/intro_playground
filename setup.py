"""
This script describes how to perform actual installation
steps: (1) install venv, (2) activate venv, (3) run setup script:
(venv3) $ python setup.py install # <-- $ is the prompt ending
To prepare distribution package:
$ python setup.py sdist --format zip # <-- setup.py says what to pkg, we chose a zip pkg format
"""

from distutils.core import setup

setup(
    name='palindrome',
    version='1.0',
    py_modules=['palindrome'],

    #metadata
    author='Some Name',
    author_email='some.name@mail.com',
    description='A sample description',
    licence='Public domain',
    keywords='example',
    )
