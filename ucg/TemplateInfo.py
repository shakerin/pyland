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
	"""

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


def Main():
	argv = docopt(__doc__)
	a = TemplateInfo("Anything", "I am $name, Who are $you. $name is me.")
	b = a.getGeneratedCode([("name", "Haha"), ("you", "None")])
	print(b)
	return


if __name__ == '__main__':
  Main()