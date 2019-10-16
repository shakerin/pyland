#!/usr/bin/python3
"""
TemplateLibrary:

Usage:
	TemplateLibrary [argv]
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
from .TemplateInfo import TemplateInfo as TI
from .FileToTemplate import FileToTemplate as FTT

class TemplateLibrary(object):
	"""TODO"""

	def __init__(self):
		pass

	def addTemplate(self, frame_string):
		pass

	def addTemplateFromFile(self, file_path):
		pass

	def readFileNames(self, dir_path):
		"""Read the directory and read all frame files to create
		templates when the script is run"""
		pass

	def execStrAsPyCmd(self, str_to_exec):
		"""executes the string as a python command after validating
		its syntax"""
		pass

	def execAllStrsAsPyCmds(self, list_of_str):
		"""ëxecutes each string of the list as python command"""
		for str_to_exec in list_of_str:
			execStrAsPyCmd(str_to_exec)
		pass

	def loadAllTemplates(self, frames_dir):
		readFileNames(frames_dir)
		pass

	def getGeneratedStr(self, frame_name, list_of_param_dicts):
		pass

	def getAllFrames(self):
		"""this method returns all frame classes created based """
		pass
	pass

	def createExtendedLibrary(self):
		"""use this method only to register frames as permanent by
		generating extended class from this class"""
		pass

