#!/usr/bin/python3
"""
FileToTemplate:

Usage:
	FileToTemplate [argv]
	Script Name: FileToTemplate.py
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





from .common_func import *
from string import Template
from docopt import docopt
import re
from .TemplateInfo import TemplateInfo

class FileToTemplate(TemplateInfo):
	"""A class used for comverting frame file into a template.
	
	This class is extended from 'TemplateInfo'. This class converts a
	text file into frame string and frame string into template.
	
	Class Attributes
	----------------
	None

	Attributes
	----------
	file_path : str
		this is the path to the frame file
	text : str
		this is the original text read from frame file

	Methods
	-------
	fileToText()
		it reads the frame file and sends the modified/unmodified text data
		to parent class 'TemplateInfo'. Currently, unmodified text
	"""






	def __init__(self, name, file_path):
		"""Reads the frame file and sends frame string to parent class

		Parameters
		----------
		file_path : str
			this is the path to the frame file
		"""


		self.file_path = file_path

		text = self.fileToText()

		super().__init__(name, text) 
















	def fileToText(self):
		"""Reads the frame file and stores as a string in 'text'"""

		text = ""

		with open(self.file_path, 'r') as f:

			text = f.read()



		return text






