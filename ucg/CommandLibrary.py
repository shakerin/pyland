#!/usr/bin/python3
"""
CommandLibrary:

Usage:
	CommandLibrary [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : October 16, 2019
	Last Modified    : <source: git>
	All Rights Reserved to Developer
"""
"""
	Script Name: TemplateLibrary.py
	Script Details: Universal Code
"""


from .common_func import *
from string import Template
from docopt import docopt
import re
from os import walk
from os.path import join, isfile

from .TemplateInfo import TemplateInfo as TI
from .FileToTemplate import FileToTemplate as FTT
from .TemplateLibrary import TemplateLibrary as TL

class CommandLibrary(TL):
	# 1. this class is going to be very similar to parent class
	# 2. at least at this moment they are going to be same
	# 3. the only difference is:
	#    when using object of this class, "runGeneratedCode"
	#    method will be used instead of "getGeneratedCode"
	# 4. this class separates the command frame files from
	#    general frame files to avoid confusion
	# 5. a separate class also gives the option to extend it 
	#    in any way in future, no need to think about both 
	#    general frames and command frames.
	pass

	
