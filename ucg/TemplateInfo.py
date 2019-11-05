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
		a prefix to indicate keywords in a frame string. the method keyWords
		automatically adds \ as prefix for any escape character used as
		identifier
	key_words : list of strings
		list of keywords extracted from the frame string
	key_word_defaults : list of strings
		during creation of object of any frame, this list will 
		remain a list of empty strings, this is just an item
		left for future extension
	template : Template
		a 'Template' object; created from frame string

	Methods
	-------
	keyWords()
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
	execSections()
		from 'original' it extracts all the executable segments and store
		them in a list named 'exec_sections' and returns the list when called

	Open Issues
	-------------
		https://github.com/shakerin/pyland/issues/4
		https://github.com/shakerin/pyland/issues/10
	"""

	# TODO evaluate the necessity of names[]
	names = []

	def __init__(self, name, templateCode, identifier="$", block_identifier=("<<<",">>>")):
		"""Extracts the frame string and store information in variables
		
		Parameters
		----------
		templateCode : str
			a string that contains the text with ketwords and addressed
			as 'frame string'
		"""
		self.name = name
		self.identifier = identifier
		start, end = block_identifier
		if start == end:
			block_identifier = ("<<<",">>>")
		self.block_identifier = block_identifier
		TemplateInfo.names.append(self.name)
		self.original = templateCode
		self.templateIns()
		self.keyWords()
		self.exec_sections, self.modified_string = self.execSections(self.original)
		
	def keyWords(self):
		"""Extracts keywords from frame string and stores in 'key_words'"""
		escape_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
		if(escape_chars.search(self.identifier)):
			self.identifier = "\\"+ self.identifier
		self.key_words = []
		self.exec_sections = [] # this will contain all executable codes
		regex_cmd = r"(?<=" + self.identifier + r")\w+"
		re_key_search = re.findall(regex_cmd,self.original)
		self.key_words = list(set(re_key_search))
		self.key_word_defaults = ["" for key in self.key_words]
		return self.key_words

	def templateIns(self):
		"""Converts frame string to a 'Template' object & stores in 'template'"""
		self.template = Template(self.original)


	def getGeneratedCode(self, key_value_pairs):
		"""Returns the generated text from a provided search/replace pair

		this method, uses the dict to generate text from the stored
		'template' and returns the generated text. The search items are keywords
		of the template and replace items are any text the task caller wants to
		replace the keyword with. Existing keywords in a template class is stored
		in a list named 'key_words'

		Parameters
		----------
		key_value_pairs : dict
			a dict of structure (search:replace) where both
			search and replace are strings, i.e. {'name' : 'Sha'}

		Limitations
		-----------
		this method doesn't care if the provided key_value pair matches the
		'key_words' or not. if all key_word value is not provided, the default
		value is empty string(''). If any wrong key is provided, that will
		be just ignored.
		TODO: consider the requirement of having key_pair checker
		"""
		key_value_pairs_dict_checked = {}
		for i, key_word in enumerate(self.key_words):
			if key_word in key_value_pairs:
				key_value_pairs_dict_checked[key_word] = key_value_pairs[key_word]
			else:
				print("TemplateInfo.py : getGeneratedCode :: " + self.name + ":: key not defined ::" + key_word)
				key_value_pairs_dict_checked[key_word] = self.key_word_defaults[i]
		generated_code = self.template.substitute(key_value_pairs_dict_checked)
		return generated_code

	def runGeneratedCode(self, key_value_pairs):
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
		generated_code = self.getGeneratedCode(key_value_pairs)
		exec(generated_code)
		return self.return_vals


	def isStrPresent(self, string, search_item):
		""""this method checks if search_item is present in
		string. it returns True if present, otherwise False"""
		search_term_present = False
		if search_item in string:
			search_term_present = True
		return search_term_present


	def execSections(self, string):
		"""this method will extract all the executable sections from
		the frame string and store it in 'exec_sections' object
		variable"""
		modified_string = ""
		start_of_exec_segment, end_of_exec_segment = self.block_identifier
		list_of_lines = string.splitlines(True)
		extracted_exec_segments = []
		no_exec_segment = 0
		start_found = False
		exec_segment = ""
		for line in list_of_lines:
			if start_found:
				if (self.isStrPresent(line, end_of_exec_segment)):
					start_found = False
					no_exec_segment += 1
					extracted_exec_segments.append(exec_segment)
					exec_segment_replacement = start_of_exec_segment + " " + str(no_exec_segment) + " " + end_of_exec_segment + "\n"
					modified_string += exec_segment_replacement
					exec_segment = ""
				else:
					exec_segment += line
			else:
				if (self.isStrPresent(line, start_of_exec_segment)):
					start_found = True
				else:
					modified_string += line
		return (extracted_exec_segments, modified_string)

