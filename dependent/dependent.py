#!/usr/local/bin/python3

# Code block that allows calling sibling subdirectories
from sys import path
from os.path import dirname
path.append(dirname(path[0]))
# End code block

import primary
from lib_dependent import second

if __name__ == '__main__':
    primary.first()
    second()
