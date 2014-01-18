#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                              Mike McKerns, Caltech
#                        (C) 1997-2012  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from __future__ import absolute_import

# get version numbers, license, and long description
try:
    from .info import this_version as __version__
    from .info import readme as __doc__, license as __license__
except ImportError:
    msg = """First run 'python setup.py build' to build pox."""
    raise ImportError(msg)

__author__ = 'Mike McKerns'

__doc__ = """
""" + __doc__

__license__ = """
""" + __license__

from .shutils import shelltype, homedir, rootdir, username, sep, \
                     minpath, env, whereis, which, find, walk, where, \
                     mkdir, rmtree, shellsub
from .utils import pattern, expandvars, getvars, convert, replace, \
                   findpackage, select, selectdict, remote, \
                   parse_remote, kbytes, disk_used, index_slice, index_join


def license():
    """print license"""
    print(__license__)
    return

def citation():
    """print citation"""
    print(__doc__[-499:-140])
    return

# end of file
