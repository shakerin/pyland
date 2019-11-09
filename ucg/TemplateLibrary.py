#!/usr/bin/python3
"""
TemplateLibrary:

Usage:
	TemplateLibrary [argv]
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








class TemplateLibrary(object):
	"""a class for storing all templates in pythonic way
	
	this class will create instances of frame classes by gathering
	all frame files in python objects. Those objects can be used later
	for generating text based on the frame strings. any number of
	directories of frames can be added.

	Class Attributes
	----------------
	N/A

	Attributes
	----------
	frame_names : list of str
		each string in this list represents created frame object name,
		each frame object can be utilized to generate text from
		that particular frame string by providing necessary inputs
	
	frame_files : list of str
		each string in this list represents a frame file path,
		to update or improve a frame file, just updateing that particular
		file is enough. each time when object of this class is created,
		all the frame objects are created from those frame files

	frame_dir : list of str
		each string in this list represents a directory path, each 
		directory can contain any number of frame files. frame files
		name has to be unique irrespective of the file extension.
		i.e. example.txt, example, example.py all three file names
		will create same frame object named 'example'. so, all files
		in all directories need unique name.

	txt : any type
		this variable is kept just for getting return values after
		executing frame string's executable segments

	Methods
	-------
	loadAllTemplates()
		this method reads all the frame strings from "frame_dirs"
		by looping through each directory in the list and uses the
		method 'loadFrameFilesFromDir'. Later, it creates "FI" object for
		each frame. 'frame_names' represent the frame objects that can
		be used for generating text.

	loadFrameFilesFromDir(dir_path)
		this method reads all the frame files from the 'dir_path',
		later, created frame objects in more technical terms, create
		instance of 'FI' class to store the frame strings from the frame
		files. all frame object names are stored in 'frame_names',
		all frame file path stored in 'frame_files'. 
	
	createFrameObjects()
		based on 'frame_names' and 'frame_files' create instances of "FTT"
		class. those objects are later used for generating text. if there
		are 1000 frame_names and 1000 frame_files, 1000 frame objects will
		be created

	findFrame(frame_name)
		this method can be used for searching for particular frame path
		by providing the frame name as an argument

	addFrameDirs(frame_dirs)
		this method can be used for adding new frame_dir/s to the exisitng
		'frame_dirs' and load templates, create frame objects based on
		that

	addFrameFromFile(frame_file)
		this method can be used for generating frame object based on a 
		provided frame file path and will be included in that object

	getGeneratedCode(frame_name, key_value_pairs)
		this method replaces the keywords with the values from the
		key_value_pairs dict

	getAllCode(frame_name, string, list_of_post_exec_strings)
		this method creates the final output based on the frame object, 
		modified_string and list of generated texts from executed segments

	Restrictions
	------------
	- this class uses the name of frame files and frame object names
	  so, all file names have to be unique even if these files
	  exist in different directories. check the "frame_dir" description
	  above for more.
	"""







	def __init__(self, frame_dirs=[]):
		"""Loads templates that are inside frame_dirs
		"""
		self.frame_names = []
		self.frame_files = []
		self.frame_dirs = frame_dirs
		self.loadAllTemplates()
		pass


	def addFrameDirs(self, frame_dirs=[]):
		"""this method lets user to add 'frame_dirs' and update
		frame objects using 'loadAllTemplates' method
		
		Parameter
		---------
		frame_dirs : list of str
			each string in list represent path to a new frame_dir
		"""
		self.frame_dirs += frame_dirs
		self.frame_dirs = list(set(self.frame_dirs))
		self.loadAllTemplates()
		return

	def addFrameFromString(self, frame_name, frame_string):
		#TODO evaluate necessity
		#TODO this should also register path as 'Dynamically Created'
		#TODO not necessary (October 20, 2019)
		pass

	def addFrameFromFile(self, frame_file):
		"""this method lets user add single frame object by providing
		path to the frame file
		
		Parameters
		----------
		frame_file : str
			this string represents the path to a frame file
		"""
		if isfile(frame_file):
		  frame_name = frame_file.split(".")[0]
		  if frame_name not in self.frame_names:
			  self.frame_names.append(frame_name)
			  self.frame_files.append(frame_file)
		else:
			print(str(frame_file) + "doesn't exist")


	def loadAllTemplates(self):
		"""main task that will be called to create all frame objects"""
		for frame_dir in self.frame_dirs:
			self.loadFrameFilesFromDir(frame_dir)
		self.createFrameObjects()






	def loadFrameFilesFromDir(self, dir_path):
		"""Read the directory and read all frame files to create
		templates when the script is run"""
		frame_file_names = []
		for (directory_path, dir_names, file_names) in walk(dir_path):
			frame_file_names.extend(file_names)
			break
		raw_frame_names = [name.split(".")[0] for name in frame_file_names]
		raw_frame_files = [join(dir_path, file) for file in frame_file_names]
		for i, raw_frame_name in enumerate(raw_frame_names):
			if raw_frame_name not in self.frame_names:
				self.frame_names.append(raw_frame_name)
				self.frame_files.append(raw_frame_files[i])
			else:
				print("[" + raw_frame_name + "] already defined: New Definition Ignored")
		return



	def createFrameObjects(self):
		"""based on the 'frame_names' and 'frame_files' generates instances
		of 'FTT' to utilize those object for generating text"""
		for i, frame_name in enumerate(self.frame_names):
			cmd = "self." + frame_name + "=" + "FTT(\"" + frame_name + "\", \"" + self.frame_files[i] + "\")"
			exec(cmd)
		

	def findFrame(self, frame_name):
		"""this method returns the frame file path for a particular string if the 
		string represents a frame in the object of this class
		
		Parameters
		----------
		frame_name : str
			A string that may or may not a frame iin that particular 
			object of this class"""

		path = "Frame Not Found"
		for i,name in enumerate(self.frame_names):
			if name == frame_name:
				path = self.frame_files[i]
				break
		return path

	# key_value_pair is a list of tuples (search, replace)
	def getGeneratedCode(self, frame_name, key_value_pairs):
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
		
		Open Case
		--------- 
			https://github.com/shakerin/pyland/issues/24
		"""
		key_value_pairs_dict_checked = {}
		for i, key_word in enumerate(frame_name.key_words):
			if key_word in key_value_pairs:
				key_value_pairs_dict_checked[key_word] = key_value_pairs[key_word]
			else:
				print("TemplateLibrary.py : getGeneratedCode :: " + frame_name.name + ":: key not defined ::" + key_word)
				key_value_pairs_dict_checked[key_word] = frame_name.key_word_defaults[i]
		generated_code = frame_name.template.substitute(key_value_pairs_dict_checked)
		return generated_code


	def runExecSections(self, list_of_strings_to_exec):
		"""this method will be called to execute all the executable 
		sections one after another"""
		post_exec_txt_list = []
		for string_to_exec in list_of_strings_to_exec:
			post_exec_txt_list.append(self.runExecSection(string_to_exec))
		return post_exec_txt_list

	def runExecSection(self, string_to_exec):
		"""this method will be called to execute only one section.
		so, this will be called from runExecSections()"""
		self.txt = ""
		string_to_exec = self.pythonify(string_to_exec)
		exec(string_to_exec)
		return self.txt

	def pythonify(self, string_to_exec):
		# TODO no use for now
		string_to_exec = self.pythonifyVars(string_to_exec)
		return string_to_exec

	def pythonifyVars(self, string_to_exec):
		"""
		there are three types of variables that can be declared
		1. local to segment - only accessible within a segment
			__var__ is prefix
			i.e. __var__name
			__var__name should be replaced by self.name and deleted
			after segment execution 

		2. local to frame string but global to segment - accessible 
		   within a frame string
		   __local__ is prefix
		   i.e. __local__name
		   __local__name should be replaced by self.name and deleted
		   after frame string execution 

		3. global to all frames
		   __global__ is prefix
		   i.e. __global__name
		   __global__name should be replaced by self.name and will 
		   never be deleted
		"""
		return string_to_exec


	def printHere(self, string_to_exec):
		"TODO will be removed in future"
		exec_cmd = "self.txt += \"" + string_to_exec + "\\n\""
		exec(exec_cmd)
		return

	def getAllCode(self, frame_name, string, list_of_post_exec_strings):
		"""this method replaces replacements of the executable segments with 
		executed sections

		each frame object has got internal variable named 'modified_string'.
		The difference between orignal frame string and modified_string is -
		in case of modified string the executable segments are replaced with
		'single line text' that can be replaced later with the generated code
		after executing the executable segments

		this method receives the modified string as an input named 'string'
		and generated code after execution of executable segments as list
		of strings named 'list_of_post_exec_string'

		this method, replaces each 'single line text' with each item in the
		list. This list is prepared from another method. For this class,
		getAll() method is doing that.

		After replacing, this method returns the final generated code for that
		file.

		Parameters
		----------
		frame_name : frame Object
			this has to be a frame object name; the frame object has to be 
			declared in this class

		string : str
			this is the modified string that is found after calling the frame 
			object method named 'execSections'

		list_of_post_exec_strings : list of str
			each string in this list corresponds to generated text or code 
			for each executable segment present in that frame string; string
			will be empty if that particular executable segment do not 
			generate any text to be copied in its place.
		"""
		string_to_use = string
		no_exec_segment = 0
		for i, post_exec_strings in enumerate(list_of_post_exec_strings):
			no_exec_segment += 1
			start, end = frame_name.block_identifier
			exec_segment_replacement = start + " " + str(no_exec_segment) + " " + end
			string_to_use = re.sub(exec_segment_replacement, list_of_post_exec_strings[i], string_to_use)
		return string_to_use

	def getAll(self, frame_name, key_value_pairs):
		"""this method will call both generatedCOde method and
		execute code method and return the final code to something

		this method, first replaces all the key_words with replacement
		strings based on the key_value_pairs,

		then, it calls the execSections() method of the frame object to
		get the executable_segments(a list of strings) and modified_string
		(a string with single line replacement texts for each executable
		segments).

		all segments present in executable_segments list are executed and
		return data is stored in another list named post_exec_txt_list

		Finally, getAllCode method is called to use modified_string and
		post_exec_txt_list to generate the final text

		Parameters
		----------		
		frame_name : frame object
			this is a frame object that is created in this class

		key_value_pairs : dict
			a dict of structure (search:replace) where both
			search and replace are strings, i.e. {'name' : 'Sha'}
			this is required for generating the text from frame string
			properly
		"""
		generated_code = frame_name.getGeneratedCode(key_value_pairs)
		executable_segments, modified_string = frame_name.execSections(generated_code)
		post_exec_txt_list = self.runExecSections(executable_segments)
		final_code = self.getAllCode(frame_name, modified_string, post_exec_txt_list)
		return final_code

