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
from .global_vars import *

class TemplateInfo(object):
	"""A class used for converting frame string into a template.
	
	This class has got internal methods and variables to store internal 
	information about the template.
	
	Class Attributes
	----------------

	Attributes
	----------
	name : str
		this is the name of the template
	original : str
		raw frame string provided from class user
	modified_string : str
		this string is created from the original string by replacing executable
		segments with identifiable string just to replace is future when 
		executable segments are executed by user class of this frame object
	identifier : str
		a prefix to indicate keywords in a frame string. the method keyWords
		automatically adds \ as prefix for any escape character used as
		identifier
	block_identifier : tuple of two strings
		first string represents the starting string to identify a executable
		segment, second string represents the end
	key_words : list of strings
		list of keywords extracted from the frame string
	key_word_defaults : list of strings
		during creation of object of any frame, this list will 
		remain a list of empty strings, this is just an item
		left for future extension
	template : Template
		a 'Template' object; created from frame string
	exec_var_local : list of strings
		each string represents a frame local variable
	exec_var_global : list of strings
		each string represents a frame global variable
	exec_sections : list of strings
		each segment represents an executable segment of the frame string

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
		self.original = templateCode
		self.templateIns()
		self.keyWords()
		self.execSections(self.original)
		
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
		self.last_generated_code = generated_code
		return self.last_generated_code

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
					exec_segment_replacement = start_of_exec_segment + " " + str(no_exec_segment) + " " + end_of_exec_segment
					modified_string += exec_segment_replacement
					if "\n" in line:
						modified_string += "\n"
					exec_segment = ""
				else:
					exec_segment += line
			else:
				if (self.isStrPresent(line, start_of_exec_segment)):
					start_found = True
				else:
					modified_string += line
		self.exec_sections = extracted_exec_segments
		self.modified_string = modified_string
		self.analyzeExecVars()
		self.pythonifyExecSections()
		return (self.exec_sections, self.modified_string)

	def analyzeExecVars(self):
		"""This method collects all local and global frame variables from
		all executable segments and stores them in object variables for
		easier access through objects

		Parameter
		---------
		exec_segments : list of strings
			each string in the list represents a raw executable segment of
			the frame string
		
		Returns
		-------
		(self.exec_var_local, self.exec_var_global) : a tuple of two lists
			first element of the tuple is the list of local variables of the 
			frameand second element is global varaibles of the frames
		"""
		exec_var_local_list, exec_var_global_list = [], []
		for segment in self.exec_sections:
			exec_var_basic = re.findall(r"__var__\w+", segment)
			exec_var_local = re.findall(r"__local__\w+", segment)
			exec_var_global = re.findall(r"__global__\w+", segment)
			exec_var_local_list.extend(exec_var_local)
			exec_var_global_list.extend(exec_var_global)
		exec_var_local_list = [item.replace("__local__", "") for item in exec_var_local_list]
		exec_var_global_list = [item.replace("__global__", "") for item in exec_var_global_list]
		exec_var_global_list = list(set(exec_var_global_list))
		exec_var_local_list = list(set(exec_var_local_list) - set(exec_var_global_list))
		self.exec_var_local = exec_var_local_list
		self.exec_var_global = exec_var_global_list
		return (self.exec_var_local, self.exec_var_global)
	
	def pythonifyExecSections(self):
		"""This method converts all the executable segments of this frame
		string into error-free Python code
		
		Parameter
		---------
		exec_segments : list of strings
			each string in the list represents raw executable segments that
			are present in that frame string

		Returns
		-------
		self.exec_sections : list of strings
			each string in the list is a error-free Python code that will be
			executed from any class that is using this class to create
			object of this frame.
		"""
		pythonified_exec_segments = []
		for segment in self.exec_sections:
			pythonified_exec_segment = self.pythonify(segment)
			pythonified_exec_segments.append(pythonified_exec_segment)
		self.exec_sections = pythonified_exec_segments
		return self.exec_sections

	def pythonify(self, string_to_exec):
		"""This method takes the raw frame executable segments and 
		updates it in such a way that the string become error-free
		Python code
		
		Parameter
		---------
		string_to_exec : string
			this string represents one executable segment in the frame string

		Returns
		-------
		string_to_exec : string
			this method returns a syntax error-free Python code for 
			that segment
		"""
		string_to_exec = self.pythonifyVars(string_to_exec)
		string_to_exec = self.printVars(string_to_exec)
		return string_to_exec

	def pythonifyVars(self, string_to_exec):
		"""This method updates the executable segments is such a way that
		frame variables are converted to error-free python variable codes.
	
		there are two types of variables that can be declared in a frame 
		string. They are mentioned below -

		1. local to frame string but global to segment - accessible 
		   within a frame string
		   __local__ is prefix
		   i.e. __local__name
		   __local__name should be replaced by self.name and deleted
		   after frame string execution 

		2. global to all frames
		   __global__ is prefix
		   i.e. __global__name
		   __global__name should be replaced by self.name and will 
		   never be deleted

		Parameter
		---------
		string_to_exec : string
			this string represent a executable segment inside a frame string
			this string contains modified or unmodified frame string segment.

		Returns
		-------
		string_to_exec : string
			this string is modifed version of the original frame string.
			the local and global frame vars will be converted to become
			python variables so that the executable segments contains only
			syntax error free python variable sections in segment.

		Note
		----
			Remember, the returned string may not be totally python error-free
			code yet. This method only takes care of the correct conversion
			of frame vars to Python variables
		"""
		string_to_exec = re.sub("__local__", "self.", string_to_exec)
		string_to_exec = re.sub("__global__", "self.", string_to_exec)
		return string_to_exec

	def printVars(self, string_to_exec):
		"""this method only replaces special text with predefined code
		sothat when this string is executed, it properly copies all text
		from the frame string(both executable/non-executable segments) to 
		the original output files"""
		string_to_exec = re.sub(r'__print__==(.*\w+)', r'self.txt += str(\1)', string_to_exec)
		return string_to_exec


