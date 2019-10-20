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







	def getGeneratedStr(self, frame_name, list_of_param_dicts):
		pass





	def getAllFrames(self):
		"""this method returns all frame classes created based """
		pass
	pass





	def createExtendedLibrary(self):
		"""use this method only to register frames as permanent by
		generating extended class from this class"""
		pass
