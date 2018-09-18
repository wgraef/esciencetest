#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='esciencetest',
    version='0.1.0',
    description="test",
    long_description=readme + '\n\n',
    author="Wouter Graef",
    author_email='wgraef@gmail.com',
    url='https://github.com//esciencetest',
    packages=[
        'esciencetest',
    ],
    package_dir={'esciencetest':
                 'esciencetest'},
    include_package_data=True,
    license="BSD license",
    zip_safe=False,
    keywords='esciencetest',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    install_requires=[],  # FIXME: add your package's dependencies to this list
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'recommonmark',
        'pyvoro',
        'numpy'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    }
)
