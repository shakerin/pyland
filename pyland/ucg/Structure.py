#!/usr/bin/python3
"""
Structure:

Usage:
	Structure [argv]
	Script Name: Structure.py
	Script Details: Universal Code
"""

# License
# Copyright (C) 2020  Shakerin Ahmed
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.






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
	"""A class used for creating directories and files based on 
	structure file.

	This class has got some attributes and methods for extracting
	necessary information from the structure file.

	Class Attributes
	----------------
	Attributes
	----------
	directory_sign : str
		any line in structure file that has got directory_sign, the portion
		before that string is considered a directory name
	file_sign : str
		any line in structure file that has got file_sign, the portion
		before that string is considered a file name
	struct_file_path : str
		this is the structure file path that is providing while creating 
		object of this class
	dir_paths : a list of str
		each str in the list represents a directory path and each str 
		ends with '/'
	file_paths : a list of str
		each str in the list represents a file path and each str should
		never end with '/' as it is file path
	original_list : a list of str
		the structure file is read as list of strings and all empty lines
		are deleted. so, original_list is the structure file as a list of
		non-empty strings
	cmd_names : a list of str
		each str in the list represents command section that is associated
		with directory name or file name
	file_names : a list of str
		each str is a file name - not path, just the name
	dir_names : a list of str
		each str is a directory name - not path, just the name
	positions_dir_only : a list of integers
		each integer is the number of space preceding the dir name
	positions : a list of integers
		each integer is the number of space preceding the dir name or
		file name

	Methods
	-------
	run()
		This is the one method that will do all extraction work
		for any given structure file
	formPaths()
		this method, forms the file paths and dir paths based on the
		information that is extracted from structure file by
		using extractDirFileCmdNames method
	createDirsAndFiles()
		this method will create all directories and files if not already
		created
	createDirs()
		create all directories present in self.dir_paths list if the 
		directories are not already created
	createFiles()
		create all files present in self.file_paths list if the
		files are not already created
	getOriginalStructureInList()
		this method reads the structure file as a list of strings
	extractDirFileCmdName(str_to_parse, separator)
		this method is created to extract dir or file name,
		position and cmd section
	extractDirFileCmdNames()
		this method separates directory, file and command strings in 
		different lists
	createPathFromPosition(paths_no, path_names, assume_path_is_file=False)
		This method returns list of real paths created based on the index
		numbers(paths_no) and dir or file+dir list(path_names)
	formDirPaths()
		Forms all paths to dir based on self.dir_paths
	formFilePaths()
		Forms all paths to dir based on self.file_paths
	cleanPaths(abs_file_paths, file_names)
		this method returns only the correct paths from a list of 
		extracted paths
	formPathsFromPosition(positions)
		returns list of paths from a list of positions


	Open Issues
	-----------
		https://github.com/shakerin/pyland/issues/39
		https://github.com/shakerin/pyland/issues/43
		https://github.com/shakerin/pyland/issues/45

	"""


	def __init__(self, struct_file):


		self.directory_sign = "//"
		
		self.file_sign = ",,"
		
		self.struct_file_path = struct_file
		
		self.run()
		
		return









	def run(self):
		"""This is the one method that will do all extraction work
		for any given structure file

		it calls -
			getOriginalStructureInList method,
				read structure file as a list of non-empty strings
			extractDirFileCmdNames method,
				extarct lists of dir names and file names and there
				positions in the structure to be able to generate
				the paths for individual dir and file
			formPaths method,
				based on the extracted information in the last method,
				this method will create the actual dir paths and file
				paths that needs to be created based on the structure
				file
			createDirsAndFiles,
				finally, this methods will create the dirs and files
				based on the formed dir and file paths

		"""
		
		
		self.getOriginalStructureInList()
		self.extractDirFileCmdNames()
		self.formPaths()
		self.cleanCmds()

		return











	def formPaths(self):
		"""this method, forms the file paths and dir paths based on the
		   information that is extracted from structure file by
		   using extractDirFileCmdNames method
		"""


		self.formDirPaths()
		self.formFilePaths()


		return

















	def cleanCmds(self):


		all_commands = []
		clean_dir_cmds, clean_file_cmds = self.separate_dir_n_filecmd()
		
		for i, cmd in enumerate(clean_dir_cmds):
		
			command = ("DIR", self.dir_paths[i], cmd.strip())
			all_commands.append(command)
		

		for i, cmd in enumerate(clean_file_cmds):
		
			command = ("FILE", self.file_paths[i], cmd.strip())
			all_commands.append(command)
		
		
		self.commands = all_commands
		
		
		return













	def separate_dir_n_filecmd(self):
		"""This method is going to be used for returning file and
		dir commands separately
		"""


		clean_dir_cmds = []
		clean_file_cmds = []

		for i, cmd in enumerate(self.cmd_names):

			if self.cmd_types[i] == "DIR":

				clean_dir_cmds.append(cmd)


			elif self.cmd_types[i] == "FILE":

				clean_file_cmds.append(cmd)


			else:

				pass



		return (clean_dir_cmds, clean_file_cmds)

















	def getOriginalStructureInList(self):
		"""this method reads the structure file as a list of strings

		the returned list after reading the structure file is saved in 
		an object attribute named 'original_list',
		this list doesn't contain any empty item.
		"""


		with open(self.struct_file_path, 'r') as f:

			original_list = f.readlines()


		original_list = list(filter(None, original_list))
				
		original = "____".join(original_list)
		self.original = re.sub(r'{.*?}', lambda x:x.group().replace("\n", "").replace("____", ""), original, flags=re.DOTALL)
		self.original_list = self.original.split("____")

		return











	def extractDirFileCmdName(self, str_to_parse, separator):
		"""this method is created to extract dir or file name,
		position and cmd section

		Parameter
		---------
		str_to_parse: a string
			this string represents any string in the structure file
			that contains either dir name or file name
		separator: a string
			it is the indicator string that identifies preceding text
			is a dir name or file
			i.e. by default, in this class, 
				separator for dir name is       //
				separator for file name is      ,,
				dir1// means, dir1 is a dir name
				file1,, means, file1 is a file name

		Returns
		-------
		(dir_file_name, dir_file_name_pos, cmd_name) : a tuple
			dir_file_name is the string that represents the dir or 
			file name,
			dir_file_name_pos is the integer that represents the
			position of the dir or file string. In other words, this 
			number indicated number of spaces preceding that dir or file
			name in that particular line in the stucture file,
			cmd_name is the string that represents the portion in
			string that contains command information
		"""



		dir_file_name = str_to_parse.strip().split(separator)[0]


		dir_file_name_raw = str_to_parse.split(separator)[0]
		dir_file_name_raw_clean = dir_file_name_raw.strip()
		dir_file_name_pos = len(dir_file_name_raw)-len(dir_file_name_raw_clean)


		cmd_name = str_to_parse.strip().split(separator)[1]		



		return (dir_file_name, dir_file_name_pos, cmd_name)








	def extractDirFileCmdNames(self):
		"""this method separates directory, file and command strings in 
		different lists

		Following attributes are created based on the structure file,
			1.  <file_names>
			    it is a list of strings where each string is a filename,
			    not file path
			2.  <dir_names>
				a list of strings where each string is a dirname,
				not a dir path
			3.  <file_n_dir_names>
				a list of strings where each string is a file or dir name,
				not file/dir path
			4.  <positions_dir_only>
				a list of integers where each integer is the number of 
				spaces present before the dir name in structure file,
				len(positions_dir_only)==len(dir_names)
			5.  <positions>
				a list of integers where each integer is the number of 
				spaces present before the dir name or file name in a 
				structure file,
				len(positions)==len(file_n_dir_names)
		"""





		dir_names, file_names, file_n_dir_names, cmd_names, cmd_types = [], [], [], [], []
		positions_dir_only, positions = [], []


		for line in self.original_list:

			if self.directory_sign in line:

				dir_name, no_of_preceding_space, cmd_name = self.extractDirFileCmdName(line, self.directory_sign)

				dir_names.append(dir_name)
				positions_dir_only.append(no_of_preceding_space)

				file_n_dir_names.append(dir_name)
				positions.append(no_of_preceding_space)

				cmd_types.append("DIR")
				cmd_names.append(cmd_name)				


			elif self.file_sign in line:

				file_n_dir_name, no_of_preceding_space_all, cmd_name = self.extractDirFileCmdName(line, self.file_sign)

				file_names.append(file_n_dir_name)

				file_n_dir_names.append(file_n_dir_name)
				positions.append(no_of_preceding_space_all)	

				cmd_types.append("FILE")
				cmd_names.append(cmd_name)


			else:
				pass






		self.cmd_types = cmd_types

		self.cmd_names = cmd_names

		self.file_names = file_names			
		
		self.dir_names = dir_names
		
		self.positions_dir_only = positions_dir_only
		
		self.file_n_dir_names = file_n_dir_names
		
		self.positions = positions
		
		
		return



















	def createPathFromPosition(self, paths_no, path_names, assume_path_is_file=False):
		"""This method returns list of real paths created based on the index
		numbers(paths_no) and dir or file+dir list(path_names) 

		Parameters
		----------
		paths_no : a list of integers
			each integer in the list represent the index of a dir/file name
			depending on the situation
		path_names: a list of strings
			each string in the list represents a file name or dir name
		assume_path_is_file : boolean
			if this boolean value is True,
				the last character of the path will be removed,
				it is done to accomodate special case in file path extraction,
				file names end with '/' just like a dir name, so, '/' at
				the end of the file path is removed based on this boolean
			else
				nothing will happen

		Returns
		-------
		dir_paths : list of strings
			each string represents a dir or file path,
			this list may contain duplicate items
		"""



		dir_paths = []

		for path in paths_no:

			abs_path = ""

			for i in path:

				abs_path += path_names[i]+"/"


			if assume_path_is_file:

				abs_path = abs_path[:-1]


			dir_paths.append(abs_path)


		if assume_path_is_file:

			dir_paths = self.cleanPaths(dir_paths, self.file_names)


		return dir_paths

















	def formDirPaths(self):
		"""Forms all paths to dir based on self.dir_paths
		
		self.dir_paths contains all directory paths"""


		paths_no = self.formPathsFromPosition(self.positions_dir_only)



		self.dir_paths = self.createPathFromPosition(paths_no, self.dir_names)



		return
















	def formFilePaths(self):
		"""Forms all paths to dir based on self.file_paths
		
		self.file_paths contains all file paths"""



		paths_no = self.formPathsFromPosition(self.positions)


		abs_file_paths = self.createPathFromPosition(paths_no, self.file_n_dir_names, True)
		abs_file_paths = getUniqueOrderedList(abs_file_paths)
		abs_file_paths = getOnlyUniqueItems(abs_file_paths, self.dir_paths)


		self.file_paths = [f[:-1] for f in abs_file_paths]


		return


















	def cleanPaths(self, abs_file_paths, file_names):
		"""this method returns only the correct paths from a list of 
		extracted paths

		it searches for 'filename'+'/' in each item of abs_file_paths and 
		replaces the string with ''.

		Parameters
		----------
		abs_file_paths : a list of strings
			each string in the list represents a path (directory or file)
			i.e. ['/home/user/filename.txt', '/home/user/']

		file_names : a list of strings
			each string in the list represents a file name
			i.e. ['filename.txt']

		Returns
		-------
		clean_abs_file_paths : a list of strings
			each string in the list represent a clean file path
		Note
		----
		the returned list may contain duplicate item
		"""



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
		"""returns list of paths from a list of positions

		Parameters
		----------
		positions : a list of integers
			each integer in the list represents position of a path in
			structure file. i.e. [0, 2, 4, 0]

		Return
		------
		paths_no : a list of integer lists
			each list in this list represent a path.

		Example
		-------
		Let say, a structure file looks like this:
		############## structure.txt #############
		dir1//
			file1.txt,,
			dir2//
		dir3//
		############## structure.txt #############
		Then, positions = [0, 4, 4, 0] where,
						   0 ---------> position of dir1 in the file
							  4 ---------> position of file1.txt in the file
							  4 ---------> position of dir2 in the file
						   0 ---------> position of dir3 in the file
		paths_no = [
					[0],  ---------> represents position of dir1 in 
									 the list positions that is [0]
					[0,1],---------> represents position of [dir1, file1.txt]
									 in the list positions that is [0,1]
					[0,2],---------> position of [dir1, dir2] in positions
					[3]   ---------> position of [dir3] in positions
					]
		If users keep the directory and filenames in a list such as:
				['dir1', 'file1.txt', 'dir2', 'dir3'], 
				they can easily create the paths from paths_no
		"""




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

