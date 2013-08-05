"""
Convert LESS to Sass. Quick-and-dirty - this is not meant to be more than
a quick hack. Output won't be perfect.

-bjp 2013-08-05
"""

import sys
import re

identifier_pat = r'[_a-zA-Z][_a-zA-Z0-9-]*'


print r'@({})'.format(identifier_pat)


def convert(src):
    # Verbatim impl of steps at:
    # https://github.com/jlong/sass-twitter-bootstrap#sass-conversion-quick-tips
    src = re.sub(r'@({})'.format(identifier_pat), r'$\1', src)
    src = re.sub(r'\.({})'.format(identifier_pat), r'@include \1', src)
    src = re.sub(r'\bspin\b', r'adjust-hue', src)
    src = re.sub(r'^(\s*@{}:.*);'.format(identifier_pat), r'\1 !default;', src)
    src = re.sub(r'^(\s*@{}:.*);'.format(identifier_pat), r'\1 !default;', src)
    # Handle #gradient > .vertical, #grid > .style, and so on
    src = re.sub(r'#{} > .{}'.format(
        identifier_pat, identifier_pat), r'@include \1-\2', src)
    src = re.sub(r'\bfadein\b', r'fade-in', src)
    # Remaining steps are manual
    return src


def convert_file(filename, backup=False):
    src = None
    with open(filename) as f:
        src = f.read()
    src = convert(src)
    with open(filename, 'w') as f:
        f.write(src)
    # TODO backup

for f in sys.argv[1:]
    convert_file(f)

# x = raw_input()
# while x:
#     print convert(x)
#     x = raw_input()
