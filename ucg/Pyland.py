#!/usr/bin/python3
"""
Pyland:

Usage:
	Pyland [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : December 28, 2019
	Last Modified    : <source: git>
	All Rights Reserved to Developer
"""
"""
	Script Name: Pyland.py
	Script Details: Universal Code
"""


from docopt import docopt
import re
from os import walk
from os.path import join, isfile

from .TemplateInfo import TemplateInfo as TI
from .TemplateLibrary import TemplateLibrary as TL
from .FileToTemplate import FileToTemplate as FTT
from .Structure import Structure
from .global_vars import *






class Pyland(object):
	"""
	- This class is the top most level of class in Pyland project.
	- Every high level or user-end methods will be defined in this class.
	- It will have methods to automate Structure and Frames.
	- Automating structure means, creating all files and directories based on
	  structure file
	- Automating frame means, executing frameObj. This can also be called 
	  frame cmd.
	"""
	def __init__(self):
		pass
	

	def automateStructure(self):
		self.St1 = Structure(STRUCT_FILE)
		self.St1.automate()
		
	def automateFrame(self):
		pass


























