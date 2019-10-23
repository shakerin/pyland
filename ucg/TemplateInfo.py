#!/usr/bin/python3
"""
TemplateInfo:

Usage:
	TemplateInfo [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : September 30, 2019
	Last Modified    : <source: git>
	All Rights Reserved to Developer
"""
"""
	Script Name: TemplateInfo.py
	Script Details: Universal Code
"""


from .common_func import *
from string import Template
from docopt import docopt
import re


class TemplateInfo(object):
	"""A class used for converting frame string into a template.
	
	This class has got internal methods and variables to store internal 
	information about the template.
	
	Class Attributes
	----------------
	names : list of strings
		this variable will keep all the template class names

	Attributes
	----------
	name : str
		this is the name of the template
	original : str
		raw frame string provided from class user
	identifier : str
		a prefix to indicate keywords in a frame string.
	key_words : list of strings
		list of keywords extracted from the frame string
	template : Template
		a 'Template' object; created from frame string

	Methods
	-------
	keyWords(identifier="$")
		extracts keywords from frame string, stores in 'key_words', 
		returns 'key_words' as well
	templateIns()
		create 'Template' objects from frame string and stores it in 'template'
	getGeneratedCode(key_value_pairs)
		based on 'key_value_pairs', generate text using the 'template' already
		created from frame string and return the generated text
	runGeneratedCode(key_value_pairs)
		based on 'key_value_pairs', generate text by calling getGeneratedCode()
		method and execute the returned text as command; user has to be very
		very careful when using this method. command must be tested before 
		using this method since this method doesn't have any fault command
		checking mechanism
	"""

	# TODO evaluate the necessity of names[]
	names = []

	def __init__(self, name, templateCode):
		"""Extracts the frame string and store information in variables
		
		Parameters
		----------
		templateCode : str
			a string that contains the text with ketwords and addressed
			as 'frame string'
		"""
		self.name = name
		TemplateInfo.names.append(self.name)
		self.original = templateCode
		self.templateIns()
		self.keyWords()

	def keyWords(self, identifier="$"):
		"""Extracts keywords from frame string and stores in 'key_words'

		Parameters
		----------
		identifier : str
			a prefix that indicates following word is a keyword,
			i.e. $i_am_keyword
		"""
		self.identifier = identifier
		self.key_words = []
		re_key_search = re.findall(r'(?<=\$)\w+',self.original)
		self.key_words = list(set(re_key_search))
		return self.key_words

	def templateIns(self):
		"""Converts frame string to a 'Template' object & stores in 'template'"""
		self.template = Template(self.original)


	# key_value_pair is a list of tuples (search, replace)
	def getGeneratedCode(self, key_value_pairs):
		"""Returns the generated text from a provided search/replace pair

		this method, uses the list of tuples to generate text from the stored
		'template' and returns the generated text. The search items are keywords
		of the template and replace items are any text the task caller wants to
		replace the keyword with. Existing keywords in a template class is stored
		in a list named 'key_words'

		Parameters
		----------
		key_value_pairs : list of tuples
			a list of tuples of structure (search, replace) where both
			search and replace are strings, i.e. [('name', 'Sha')]
		"""
		key_value_pairs_dict = {}
		for key_value in key_value_pairs:
			key, value = key_value
			key_value_pairs_dict[key] = value
		generated_code = self.template.substitute(key_value_pairs_dict)
		return generated_code

	def runGeneratedCode(self, key_value_pairs):
		"""Executes the generated text based on key_value_pairs as python
		command.

		this method, uses the list of tuples to generate text from the stored
		'template'. this method uses the 'getGeneratedCode()' method to 
		generate the text. after getting the generated text, it executes that
		text as python command. this method doesn't return anything.

		Parameters
		----------
		key_value_pairs : list of tuples
			a list of tuples of structure (search, replace) where both
			search and replace are strings, i.e. [('i', "1")]

		Restriction
		-----------
		- user must be careful while using this method
		- this method doesn't check if the generated text is free 
	      from syntax errors
		- user must confirm generated text is syntax error free
	      python command before using this method
		"""
		generated_code = self.getGeneratedCode(key_value_pairs)
		exec(generated_code)
		return
