from __future__ import division, print_function

import os
import sys
from atexit import register
from cStringIO import StringIO
from itertools import ifilter, imap, izip

#region py3k
input = lambda: sys.stdin.readline().rstrip('\r\n')
range = xrange
filter, map, zip = ifilter, imap, izip

#endregion

#region fastio
input = StringIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
