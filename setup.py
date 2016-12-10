#!/usr/bin/env python

from setuptools import setup

version = __import__('csscolor').__version__

setup(
    name='csscolor',
    packages=[
        'csscolor'
        ],

    version=version,
    description='CSS colors and parsing.',
    author='Ian Millington',
    author_email='idmillington@googlemail.com',

    url='http://github.com/idmillington/csscolor',
    download_url='https://github.com/idmillington/csscolor/tarball/master',

    keywords=['csscolor', 'css', 'color', 'colour'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        ],

    zip_safe=False,

    # Testing and documentation requirements can be installed with:
    # pip install -r dev-requirements.txt
    install_requires=[]
    )
