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
from .common_func import *



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
	def __init__(self, struct_file):
		self.frame_dir_list = DEFAULT_FRAME_DIR_LIST + USER_FRAME_DIR_LIST
		self.automateStructure(struct_file)
		pass
	

	def automateStructure(self, struct_file):
		self.ST1 = Structure(struct_file)
		self.automate()
		
	def automate(self):
		self.createDirsAndFiles()
		pass

	
	
	def createDirsAndFiles(self):
		"""this method will create all directories and files if not already
		created"""
		self.createDirs()
		self.createFiles()
		return

	def createDirs(self):
		"""create all directories present in self.dir_paths list if the 
		directories are not already created"""
		for path in self.ST1.dir_paths:
			createDirIfNotPresent(path)
		return

	def createFiles(self):
		"""create all files present in self.file_paths list if the
		files are not already created"""
		for path in self.ST1.file_paths:
			createFileIfNotPresent(path)
		return


	def execCmds(self):
		"""
		ins_14= TL([PV_testdir_Discrete_Examples])
        generated_code = ins_14.getAll(ins_14.frame_with_exec_seg_assign_var_version2,
                                      {
                                        'name':'EXAMPLE',
                                        'anything':'FILE',
                                        'language':'PYTHON'
                                       })
		"""
		pass























