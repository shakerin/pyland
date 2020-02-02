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
		self.extractDirFileCmdNames()
		self.createAbsPaths()
		self.createDirectoryAndFiles()
		return

	def createAbsPaths(self):
		self.createAbsDirPaths()
		self.createAbsFilePaths()
		return


	def createDirectoryAndFiles(self):
		self.createDirs()
		self.createFiles()
		return

	def createDirs(self):
		"""self.abs_paths"""
		for path in self.abs_paths:
			createDirIfNotPresent(path)
		return

	def createFiles(self):
		"""self.abs_filepaths"""
		for path in self.abs_filepaths:
			createFileIfNotPresent(path)
		return


	def getOriginalStructureInList(self):
		with open(self.struct_file_path, 'r') as f:
			original_list = f.readlines()
		self.original_list = list(filter(None, original_list))
		return


	def extractDirFileNameCmd(self, str_to_parse, separator):
		dir_file_cmd_name = str_to_parse.strip().split(separator)[0]
		dir_file_cmd_name_raw = str_to_parse.split(separator)[0]
		dir_file_cmd_name_raw_clean = dir_file_cmd_name_raw.strip()
		dir_file_cmd_name_pos = len(dir_file_cmd_name_raw)-len(dir_file_cmd_name_raw_clean)
		return (dir_file_cmd_name, dir_file_cmd_name_pos)

	def extractDirFileCmdNames(self):
		dir_names, file_names, file_n_dir_names = [], [], []
		no_of_preceding_spaces, no_of_preceding_spaces_all = [], []
		for line in self.original_list:
			if self.directory_sign in line:
				dir_name, no_of_preceding_space = self.extractDirFileNameCmd(line, self.directory_sign)
				dir_names.append(dir_name)
				no_of_preceding_spaces.append(no_of_preceding_space)
				file_n_dir_names.append(dir_name)
				no_of_preceding_spaces_all.append(no_of_preceding_space)				
			elif self.file_sign in line:
				file_n_dir_name, no_of_preceding_space_all = self.extractDirFileNameCmd(line, self.file_sign)
				no_of_preceding_spaces_all.append(no_of_preceding_space_all)	
				file_n_dir_names.append(file_n_dir_name)
				file_names.append(file_n_dir_name)
		self.file_names = file_names			
		self.dir_names = dir_names
		self.no_of_preceding_spaces = no_of_preceding_spaces
		self.file_n_dir_names = file_n_dir_names
		self.no_of_preceding_spaces_all = no_of_preceding_spaces_all
		return


	def getAbsPaths(self, paths_no, path_names, assume_path_is_file=False):
		abs_paths = []
		for path in paths_no:
			abs_path = ""
			for i in path:
				abs_path += path_names[i]+"/"
			if assume_path_is_file:
				abs_path = abs_path[:-1]
			abs_paths.append(abs_path)
		if assume_path_is_file:
			abs_paths = self.getOnlyFilePaths(abs_paths, self.file_names)
		return abs_paths


	def createAbsDirPaths(self):
		"""self.abs_paths contains all directory paths"""
		paths_no = self.formPathsFromPosition(self.no_of_preceding_spaces)
		self.abs_paths = self.getAbsPaths(paths_no, self.dir_names)
		return

	def createAbsFilePaths(self):
		"""self.abs_filepaths contains all file paths"""
		paths_no = self.formPathsFromPosition(self.no_of_preceding_spaces_all)
		abs_file_paths = self.getAbsPaths(paths_no, self.file_n_dir_names, True)
		abs_file_paths = list(set(abs_file_paths) - set(self.abs_paths))
		self.abs_filepaths = [f[:-1] for f in abs_file_paths]
		return


	def getOnlyFilePaths(self, abs_file_paths, file_names):
		clean_abs_file_paths = []
		file_names = list(set(file_names))
		file_name_regex = "/|".join(file_names)
		file_name_regex = file_name_regex+"/" if file_name_regex != "" else "XXXXXXXXXXXXXXXXX"
		for abs_file_path in abs_file_paths:
			clean_file_name = ""
			clean_file_name = re.sub(file_name_regex, '', abs_file_path) + "/"
			clean_abs_file_paths.append(clean_file_name)
		return clean_abs_file_paths

	def formPathsFromPosition(self, positions):
		paths_no = []
		for i, position in enumerate(positions):
			segment = list(reversed(positions[:i+1]))
			a1 = segment[0]
			path = []
			for j, pos in enumerate(segment[1:]):
				if len(segment) < 2:
					pass
				else:
					a2 = pos
					if a1>a2:
						a1 = a2
						path.append(len(segment[1:])-1-j)# path ==> [0, 2, 3]
			path = list(reversed(path))
			path.append(i)
			paths_no.append(path)
		return paths_no



	def executeFrameObj(self, frameObj):
		"""this will execute the frame object"""
		pass

	
	def automate(self):
		pass
