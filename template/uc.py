#!/usr/bin/python3
"""
uc:

Usage:
	uc [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : September 30, 2019
	Last Modified    :
	All Rights Reserved to Developer
"""
"""
	Script Name: uc.py
	Script Details: Universal Code
"""


import common_func as cf
from string import Template
from docopt import docopt
import re


class TemplateInfo(object):
	"""docstring for TemplateInfo"""
	def __init__(self, templateCode):
		super(TemplateInfo, self).__init__()
		self.original = templateCode
		self.templateIns()
		self.keyWords()

	def keyWords(self, identifier="$"):
		self.key_words = []
		re_key_search = re.findall(r'(?<=\$)\w+',self.original)
		self.key_words = list(set(re_key_search))
		return self.key_words

	def templateIns(self):
		self.template = Template(self.original)


	# key_value_pair is a list of tuples (search, replace)
	def getGeneratedCode(self, key_value_pairs):
		key_value_pairs_dict = {}
		for key_value in key_value_pairs:
			key, value = key_value
			key_value_pairs_dict[key] = value
		generated_code = self.template.substitute(key_value_pairs_dict)
		return generated_code


class FileToTemplate(TemplateInfo):
	"""docstring for FileToTemplate"""
	def __init__(self, file_path):
		self.file_path = file_path
		self.fileToText()
		super(FileToTemplate, self).__init__(self.text)


	def fileToText(self):
		with open(self.file_path, 'r') as f:
			self.text = f.read()

						
def Main():
	argv = docopt(__doc__)
	#a = TemplateInfo("I am $name, Who are $you. $name is me.")
	a = FileToTemplate("./test_template")
	b = a.getGeneratedCode([("name", "Shakerin"), ("you", "Jessy")])
	print(b)
	return


if __name__ == '__main__':
  Main()