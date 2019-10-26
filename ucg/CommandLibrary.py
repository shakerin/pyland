#!/usr/bin/python3
"""
CommandLibrary:

Usage:
	CommandLibrary [argv]
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
from os.path import join, isfile

from .TemplateInfo import TemplateInfo as TI
from .FileToTemplate import FileToTemplate as FTT
from .TemplateLibrary import TemplateLibrary as TL

class CommandLibrary(TL):
	"""
	Open Issues
	-------------
		https://github.com/shakerin/pyland/issues/9
	"""
	# 1. this class is going to be very similar to parent class
	# 2. at least at this moment they are going to be same
	# 3. the only difference is:
	#    when using object of this class, "runGeneratedCode"
	#    method will be used instead of "getGeneratedCode"
	# 4. this class separates the command frame files from
	#    general frame files to avoid confusion
	# 5. a separate class also gives the option to extend it 
	#    in any way in future, no need to think about both 
	#    general frames and command frames.
	pass

	def runGeneratedCode(self, cmd_frame_name, key_value_pairs):
		"""Executes the generated text based on key_value_pairs as python
		command and returns 'return_vals' after execution of command

		this method, uses the dict to generate text from the stored
		'template'. this method uses the 'getGeneratedCode()' method to 
		generate the text. after getting the generated text, it executes that
		text as python command. this method returns 'return_vals' after execution
		of command. 'return_vals' by default is empty string. It can be anything
		based on how the command frame file is created

		Parameters
		----------
		key_value_pairs : dict
			a dict structure (search:replace) where both
			search and replace are strings, i.e. {'i' : "1"}

		Restriction
		-----------
		- user must be careful while using this method
		- this method doesn't check if the generated text is free 
	      from syntax errors
		- user must confirm generated text is syntax error free
	      python command before using this method
		"""
		self.return_vals = ""
		generated_code = self.getGeneratedCode(cmd_frame_name, key_value_pairs)
		exec(generated_code)
		return self.return_vals

	
