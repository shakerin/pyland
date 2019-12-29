#!/usr/bin/python3
"""
Structure:

Usage:
	Structure [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : December 28, 2019
	Last Modified    : <source: git>
	All Rights Reserved to Developer
"""
"""
	Script Name: Structure.py
	Script Details: Universal Code
"""


from docopt import docopt
import re
from os import walk
from os.path import join, isfile

from .TemplateInfo import TemplateInfo as TI
from .TemplateLibrary import TemplateLibrary as TL
from .FileToTemplate import FileToTemplate as FTT
from .global_vars import *



class Structure(object):
	"""
	Purpose of this class is to extract a FrameDir file,
	create directories,
	create files,
	generate frame texts inside files,
	execute texts from frames
	"""


    def __init__(self, struct_file):
		self.frame_dir_list = DEFAULT_FRAME_DIR_LIST + USER_FRAME_DIR_LIST
		self.TL_ins = TL(self.frame_dir_list)
		self.directory_sign = "//"
		self.file_sign = ",,"
        pass

	def executeFrameObj(self, frameObj):
		"""this will execute the frame object"""
		pass


    def automate(self):
        pass
