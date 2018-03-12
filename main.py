#!/usr/local/bin/python3

# Code block that allows calling sibling subdirectories
from sys import path
from os.path import dirname
path.append(dirname(path[0]))
# End code block

import primary

if __name__ == '__main__':
    primary.first()
    primary.second()
