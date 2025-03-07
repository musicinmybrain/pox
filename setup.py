#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2022 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/pox/blob/master/LICENSE

import os
import sys
# drop support for older python
unsupported = None
if sys.version_info < (2, 7):
    unsupported = 'Versions of Python before 2.7 are not supported'
elif (3, 0) <= sys.version_info < (3, 7):
    unsupported = 'Versions of Python before 3.7 are not supported'
if unsupported:
    raise ValueError(unsupported)

# get distribution meta info
here = os.path.abspath(os.path.dirname(__file__))
meta_fh = open(os.path.join(here, 'pox/__init__.py'))
try:
    meta = {}
    for line in meta_fh:
        if line.startswith('__version__'):
            VERSION = line.split()[-1].strip("'").strip('"')
            break
    meta['VERSION'] = VERSION
    for line in meta_fh:
        if line.startswith('__author__'):
            AUTHOR = line.split(' = ')[-1].strip().strip("'").strip('"')
            break
    meta['AUTHOR'] = AUTHOR
    LONG_DOC = ""
    DOC_STOP = "FAKE_STOP_12345"
    for line in meta_fh:
        if LONG_DOC:
            if line.startswith(DOC_STOP):
                LONG_DOC = LONG_DOC.strip().strip("'").strip('"').lstrip()
                break
            else:
                LONG_DOC += line
        elif line.startswith('__doc__'):
            DOC_STOP = line.split(' = ')[-1]
            LONG_DOC = "\n"
    meta['LONG_DOC'] = LONG_DOC
finally:
    meta_fh.close()

# get version numbers, long_description, etc
AUTHOR = meta['AUTHOR']
VERSION = meta['VERSION']
LONG_DOC = meta['LONG_DOC'] #FIXME: near-duplicate of README.md
#LICENSE = meta['LICENSE'] #FIXME: duplicate of LICENSE
AUTHOR_EMAIL = 'mmckerns@uqfoundation.org'

# check if setuptools is available
try:
    from setuptools import setup
    from setuptools.dist import Distribution
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    Distribution = object
    has_setuptools = False

# build the 'setup' call
setup_kwds = dict(
    name='pox',
    version=VERSION,
    description='utilities for filesystem exploration and automated builds',
    long_description = LONG_DOC,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    maintainer = AUTHOR,
    maintainer_email = AUTHOR_EMAIL,
    license = '3-clause BSD',
    platforms = ['Linux', 'Windows', 'Mac'],
    url = 'https://github.com/uqfoundation/pox',
    download_url = 'https://pypi.org/project/pox/#files',
    project_urls = {
        'Documentation':'http://pox.rtfd.io',
        'Source Code':'https://github.com/uqfoundation/pox',
        'Bug Tracker':'https://github.com/uqfoundation/pox/issues',
    },
    python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    packages = ['pox','pox.tests'],
    package_dir = {'pox':'pox','pox.tests':'tests'},
    scripts=['scripts/pox'],
)

# force python-, abi-, and platform-specific naming of bdist_wheel
class BinaryDistribution(Distribution):
    """Distribution which forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

# define dependencies
dummy_version = 'dummy>=0.1'
extra_version = 'extra>=0.1'
# add dependencies
depend = [dummy_version]
extras = {'extra': [extra_version]}
# update setup kwds
if has_setuptools:
    setup_kwds.update(
        zip_safe=False,
        # distclass=BinaryDistribution,
        # install_requires=depend,
        # extras_require=extras,
    )

# call setup
setup(**setup_kwds)

# if dependencies are missing, print a warning
try:
    pass
except ImportError:
    print("\n***********************************************************")
    print("WARNING: One of the following dependencies is unresolved:")
#   print("    %s" % dummy_version)
    print("***********************************************************\n")


if __name__=='__main__':
    pass

# end of file
