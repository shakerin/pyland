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
from os import walk
from os.path import join

from .TemplateInfo import TemplateInfo as TI
from .FileToTemplate import FileToTemplate as FTT

class TemplateLibrary(object):
	"""TODO"""

	def __init__(self, frame_dirs=[]):
		self.frame_names = []
		self.frame_files = []
		self.frame_dirs = frame_dirs
		self.loadAllTemplates()
		pass

	def addTemplate(self, frame_string):
		pass

	def addTemplateFromFile(self, file_path):
		pass

	def loadFrameFilesFromDir(self, dir_path):
		"""Read the directory and read all frame files to create
		templates when the script is run"""
		frame_file_names = []
		for (directory_path, dir_names, file_names) in walk(dir_path):
			frame_file_names.extend(file_names)
			break
		raw_frame_names = [name.split(".")[0] for name in frame_file_names]
		raw_frame_files = [join(dir_path, file) for file in frame_file_names]
		for i, raw_frame_name in enumerate(raw_frame_names):
			if raw_frame_name not in self.frame_names:
				self.frame_names.append(raw_frame_name)
				self.frame_files.append(raw_frame_files[i])
			else:
				print("[" + raw_frame_name + "] already defined: New Definition Ignored")
		return

	def execStrAsPyCmd(self, str_to_exec):
		"""executes the string as a python command after validating
		its syntax"""

		pass

	def execAllStrsAsPyCmds(self, list_of_str):
		"""ëxecutes each string of the list as python command"""
		for str_to_exec in list_of_str:
			execStrAsPyCmd(str_to_exec)
		pass

	def loadAllTemplates(self):
		"""main task that will be called to create all frame objects"""
		for frame_dir in self.frame_dirs:
			self.loadFrameFilesFromDir(frame_dir)
		#createFrameObjects()
		

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

