#!/usr/bin/python3
"""
Structure:

Usage:
	Structure [argv]
"""
"""
	Developer        : Shakerin Ahmed
	Email            : shakerin.ahmed@gmail.com
	Date             : December 28, 2019
	Last Modified    : <source: git>
	All Rights Reserved to Developer
"""
"""
	Script Name: Structure.py
	Script Details: Universal Code
"""


from docopt import docopt
import re
from os import walk
from os.path import join, isfile

from .TemplateInfo import TemplateInfo as TI
from .TemplateLibrary import TemplateLibrary as TL
from .FileToTemplate import FileToTemplate as FTT
from .global_vars import *
from .common_func import *



class Structure(object):
	"""
	Purpose of this class is to extract a FrameDir file,
	create directories,
	create files,
	generate frame texts inside files,
	execute texts from frames
	"""


	def __init__(self, struct_file, frame_dir_list):
		self.directory_sign = "//"
		self.file_sign = ",,"
		self.struct_file_path = struct_file
		self.extractStructFile()
		self.frame_dir_list = frame_dir_list
		return


	def setupTemplateLibrary(self):
		self.TL_ins = TL(self.frame_dir_list)
		return



	def directoryPaths(self):
		"""This method will be used for extracting all directory paths
		that has to be created for given directory structure
		"""
		return

	def filePaths(self):
		"""This method will be used for extracting all file paths that
		has to be created for given directory structure
		"""
		return


	def extractStructFile(self):
		self.getOriginalStructureInList()
		self.extractDirNames()
		self.createAbsDirPaths()
		return


	def getOriginalStructureInList(self):
		with open(self.struct_file_path, 'r') as f:
			self.original_list = f.readlines()
		self.original_list = filter(None, self.original_list)
		return

	def extractDirNames(self):
		dir_names = []
		no_of_preceding_spaces = []
		for line in self.original_list:
			if "//" in line:
				dir_name = line.replace("//", "").strip()
				dir_names.append(dir_name)
				dir_name_segment = line.split("//")[0]
				no_of_preceding_space = len(dir_name_segment) - len(dir_name_segment.strip())
				no_of_preceding_spaces.append(no_of_preceding_space)
		self.dir_names = dir_names
		self.no_of_preceding_spaces = no_of_preceding_spaces
		return

	def createAbsDirPaths(self):
		dir_names = self.dir_names
		positions = self.no_of_preceding_spaces
		paths_no = []
		# [1, 2, 7, 3]
		for i, position in enumerate(positions):#[1, 2, 7]
			segment = list(reversed(positions[:i+1]))#[2, 1], [7, 2, 1], [3, 7, 2, 1]
			a1 = segment[0]
			path = [i]
			for j, pos in enumerate(segment[:-1]):
				#path = [j]#path ==> [0]
				if len(segment) < 2:
					pass
				else:
					a2 = segment[j+1]# j+1==> 1, 2, 3 
					if a1>a2:
						a1 = a2
						path.append(j+1)# path ==> [0, 2, 3]
			paths_no.append(path)
		abs_paths = []
		for path in paths_no:
			abs_path = ""
			for i in path:
				abs_path += dir_names[i]+"/"
			abs_paths.append(abs_path)
		self.abs_paths = abs_paths
		return



	def executeFrameObj(self, frameObj):
		"""this will execute the frame object"""
		pass

	
	def automate(self):
		pass
