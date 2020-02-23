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
	def __init__(self, frame_dirs, filepath_or_frame, output_file=""):
		self.frame_dirs = frame_dirs
		self.TL1 = TL(self.frame_dirs)
		if self.isStruct(filepath_or_frame):
			structfilepath = filepath_or_frame
			self.automateStructure(structfilepath)
		else:
			frame_cmd = filepath_or_frame
			self.automateFrame(frame_cmd, output_file)
		return
	

	def isStruct(self, file_path):
		is_struct = False
		if isfile(file_path):
			is_struct = True
		return is_struct



	def automateStructure(self, struct_file):
		self.ST1 = Structure(struct_file)
		self.automate()

	def automateFrame(self, frame_cmd, output_file=""):
		generated_code = self.execFileCmd(frame_cmd, output_file)
		self.frame_generated_code = generated_code
		
		
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
				self.execFileCmd(cmd, path)
			else:
				pass

	def execFileCmd(self, cmd, path=""):
		frame_ins_name, frame_args = self.cleanFileCmd(cmd)
		frame_name = frame_ins_name.replace("self.TL1.", "")
		if frame_name in self.TL1.frame_names:
			generated_code_cmd = self.TL1.getAll(eval(frame_ins_name), eval(frame_args))
		else:
			generated_code_cmd = "PYLAND(execFileCmd): FRAME NOT PRESENT : " + cmd
		if path != "":
			createNewFile(path, generated_code_cmd)
		return generated_code_cmd


	def cleanFileCmd(self, cmd):
		if "{" in cmd:
			frame_name = cmd.split("{")[0]
			frame_args = cmd.split("{")[1].replace("}", "")
			cmd_frame_name = "self.TL1." + frame_name
			cmd_frame_args = "{" + frame_args + "}"
		else:
			cmd_frame_name = cmd
			cmd_frame_args = {}
		return (cmd_frame_name, cmd_frame_args)


















