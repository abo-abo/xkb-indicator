#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='xkb-indicator',
    version='0.1.3',
    description='XKB indicator.',
    long_description='https://raw.githubusercontent.com/abo-abo/xkb-indicator/master/README.org',
    packages=find_packages(),
    url='https://github.com/abo-abo/xkb-indicator',
    author='Oleh Krehel',
    author_email='ohwoeowho@gmail.com',
    license='GPLv3+',
    keywords='xkb',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    install_requires=['pycook'],
    entry_points={'console_scripts': ['xkbi=xkb_indicator.xkb_indicator:main']}
)
