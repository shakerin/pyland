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
	def __init__(self, struct_file, frame_dirs=[]):
		self.automateStructure(struct_file, frame_dirs)
		pass
	

	def automateStructure(self, struct_file, frame_dirs):
		self.TL1 = TL(frame_dirs)
		self.ST1 = Structure(struct_file)
		self.automate()
		
	def automate(self):
		self.createDirsAndFiles()
		self.execCmds()
		pass

	
	
	def createDirsAndFiles(self):
		"""this method will create all directories and files if not already
		created"""
		self.createDirs()
		#self.createFiles()
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
		for cmd_tuple in self.ST1.commands:
			cmd_type, path, cmd = cmd_tuple
			if cmd_type == "FILE":
				"""justText('')"""
				self.execFileCmd(path, cmd)
			else:
				pass

	def execFileCmd(self, path, cmd):
		frame_name, frame_args = self.cleanFileCmd(cmd)
		generated_code_cmd = self.TL1.getAll(eval(frame_name), eval(frame_args))
		createFileIfNotPresent(path, generated_code_cmd)
		return


	def cleanFileCmd(self, cmd):
		frame_name = cmd.split("{")[0]
		frame_args = cmd.split("{")[1].replace("}", "")
		cmd_frame_name = "self.TL1." + frame_name
		cmd_frame_args = "{" + frame_args + "}"
		return (cmd_frame_name, cmd_frame_args)


















