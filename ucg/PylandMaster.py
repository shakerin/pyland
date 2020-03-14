#!/usr/bin/python3
"""
PylandMaster:

Usage:
	PylandMaster [argv]
	Script Name: PylandMaster.py
	Script Details: Universal Code
"""


# License
# Copyright (C) 2020  Shakerin Ahmed
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



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













class PylandMaster(object):
	"""Top level class for this tool. This class can be utilized
	to generate code based on frame command and automate directory
	structure creation based on structure file.

	Class Attributes
	----------------
	N/A

	Attributes
	----------
	frame_dirs : a list of str
		each string in the list represents a directory path,
		there can be any number of frame files in each of the
		directories,
		frame names has to be unique which means, frame file
		names should be unique. Two frame files will not be
		considered unique even if the file extensions are 
		different.

	TL1 : an object of TemplateLibrary class
		this is the template library instance that is used for
		executing frame files

	ST1 : an object of Sturcture class (only for Sturture Execution)
		this is a structure class for analyzing information
		about the structure file that is provided

	frame_generated_code : string (only for Frame Execution)
		this string represents the generated text from after
		executing the frame file

	"""






	def __init__(self, frame_dirs, filepath_or_frame, output_file="", cmd="AUTOMATE"):


		self.frame_dirs = frame_dirs
		
		self.TL1 = TL(self.frame_dirs)
		
		
		if self.isStruct(filepath_or_frame):
		
			if cmd == "AUTOMATE":
				
				self.automateStructure(filepath_or_frame)


		
		
		else:

			if cmd == "AUTOMATE":
				
				self.automateFrame(filepath_or_frame, output_file)
		
			elif cmd == "ABOUT":

				self.aboutFrame(filepath_or_frame)

			else:

				pass



		return
	



















	def isStruct(self, file_path):
		"""checking if the input provided is a structure file path or
		frame command
		
		Parameter
		---------
		file_path : a string
			this method will check if this string is an actual path or
			frame command

		Returns
		-------
		is_struct : a boolean
			True if file_path is an actual file path,
			False if file_path is not a file path
		"""


		is_struct = False

		if isfile(file_path):

			is_struct = True


		return is_struct



















	def automateStructure(self, struct_file):
		"""This method creates directory structure based on provided
		structure file

		Parameter
		---------
		struct_file : string
			this string represents path to the structure file
		"""


		self.ST1 = Structure(struct_file)

		self.automate()


















	def automateFrame(self, frame_cmd, output_file=""):
		"""This method executes the frame command provided as an 
		input.

		Parameter
		---------
		frame_cmd : string
			this string represents a frame command.

		output_file : string
			if not empty, output of the executed frame command
			will be copied in this file
		"""


		generated_code = self.execFileCmd(frame_cmd, output_file)

		self.frame_generated_code = generated_code




	def aboutFrame(self, frame_name):
		if frame_name in self.TL1.frame_names:
			frame_info = "self.TL1." + frame_name + ".key_words"
			print(eval(frame_info))
		else:
			print(frame_name, " Not Present In Template Library Paths ", self.frame_dirs)





		


	def automate(self):
		"""This method creates directories based on the structure 
		file and based on associated commands, all files will be
		created.
		"""


		self.createDirs()

		self.execCmds()












	
	def createDirs(self):
		"""create all directories present in self.dir_paths list if the 
		directories are not already created"""


		for path in self.ST1.dir_paths:

			createDirIfNotPresent(path)


		return















	def execCmds(self):
		"""Executes only the FILE type commands based on the structure file"""

		for cmd_tuple in self.ST1.commands:

			cmd_type, path, cmd = cmd_tuple


			if cmd_type == "FILE":

				self.execFileCmd(cmd, path)



		return
















	def execFileCmd(self, cmd, path=""):
		"""Executes cmd and writes output from executed command to path
		if path is not empty"""


		frame_ins_name, frame_args = self.cleanFileCmd(cmd)
		frame_name = frame_ins_name.replace("self.TL1.", "")


		if frame_name in self.TL1.frame_names:

			generated_code_cmd = self.TL1.getAll(eval(frame_ins_name), eval(frame_args))


		else:

			generated_code_cmd = "PylandMaster(execFileCmd): FRAME NOT PRESENT : " + cmd




		if path != "":

			createNewFile(path, generated_code_cmd)



		return generated_code_cmd

















	def cleanFileCmd(self, cmd):
		"""Cleans command and returns frame name and arguments in
		a way that will be evaluated in execFileCmd method
		"""


		if "{" in cmd:

			frame_name = cmd.split("{")[0]
			frame_args = cmd.split("{")[1].replace("}", "")

			cmd_frame_name = "self.TL1." + frame_name
			cmd_frame_args = "{" + frame_args + "}"


		else:

			#TODO check code
			cmd_frame_name = "self.TL1." + cmd
			cmd_frame_args = {}




		return (cmd_frame_name, cmd_frame_args)


















