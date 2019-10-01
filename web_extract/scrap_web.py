#!/usr/bin/python3
"""
scrap_web:

Usage:
	scrap_web [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : September 29, 2019
	Last Modified    :
	All Rights Reserved to Developer
"""
"""
	Script Name:
	Script Details:
"""


import common_func as cf
from docopt import docopt


def Main():
	argv = docopt(__doc__)
	print(argv)
	return



if __name__ == '__main__':
  Main()