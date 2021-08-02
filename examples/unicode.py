#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test for printing of unicode in Python 2 and 3. It should print the word
café.

Python in MSYS2's mintty does not render unicode correctly if the code page
is set to 65001 (unicode), which is the default in mintty. Also, the python2
repl will give 'LookupError: unknown encoding: cp65001' upon entering anything
at the prompt.

The simple fix is to set an envionment variable PYTHONIOENCODING=UTF-8
but this breaks unicode printing in python when the codepage is 437, which
is the default for other terminals such as windows terminal. So the complete
fix that will work in all terminals is to query the current code page and then
set the variable accordingly.

add the following to your .bashrc

if [[ $(chcp.com | awk '{printf $4}') -eq 65001 ]]; then
  export PYTHONIOENCODING=UTF-8
fi
"""

import sys
import platform

v = sys.version_info
print('Python %d.%d.%d on %s %s' %
      (v.major, v.minor, v.micro, platform.system(), platform.version()))
print(u'caf\xe9')
