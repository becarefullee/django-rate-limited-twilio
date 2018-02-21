import os
from os.path import abspath, dirname, join, normpath
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(

    # Basic package information:
    name='django-rate-limit-twilio',
    version='0.0.1',
    packages=find_packages(),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    # Package dependencies:
    install_requires=[
        'twilio==6.10.3',
        'Django>=1.8',
        'django-phonenumber-field==2.0.0'
    ],

    # Metadata for PyPI:
    long_description=README,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
    ]

)