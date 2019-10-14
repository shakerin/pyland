#!/usr/bin/python3
"""
FileToTemplate:

Usage:
	FileToTemplate [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : September 30, 2019
	Last Modified    : <source: git>
	All Rights Reserved to Developer
"""
"""
	Script Name: FileToTemplate.py
	Script Details: Universal Code
"""


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
		self.fileToText()
		super().__init__(name, self.text) 
		#TODO self.text is redundant -> remove it and don't use it


	def fileToText(self):
		"""Reads the frame file and stores as a string in 'text'"""
		with open(self.file_path, 'r') as f:
			self.text = f.read()

						
def Main():
	argv = docopt(__doc__)
	a = FileToTemplate("nothing","./test_template")
	b = a.getGeneratedCode([("name", "Haha"), ("you", "None")])
	print(b)
	return


if __name__ == '__main__':
  Main()