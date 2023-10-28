from __future__ import unicode_literals

import sys
import re
from codecs import open

filename = sys.argv[1]

with open(filename, 'rt', encoding='utf-8') as f:
    lines = list(f.readlines())

# This modules are not availabe in GAE, we don't use any of the functions
# that require them
forbidden_modules = ['fcntl', 'ctypes', 'netrc', 'ctypes']
new_lines = (re.sub(
    r'import ({})'.format('|'.join(map(re.escape, forbidden_modules))),
    r'()# Removed \1 import',
    line) for line in lines)

with open(filename, 'wt', encoding='utf-8') as f:
    f.writelines(new_lines)
