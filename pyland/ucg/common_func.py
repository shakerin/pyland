#!/usr/bin/python3


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







"""
Function List:
1) printList(user_list)
		prints items of list one by one
2) printListN(user_list)
		prints items of a list one by one and numbered
3) printDict(user_dict)

"""

import os
import shutil
from pathlib import Path








# prints items of list one by one
def printList(user_list):


	for item in user_list:

		print(str(item))


	return










# prints items of a list one by one and numbered
def printListN(user_list):


	for i,item in enumerate(user_list):

		print(str(i+1)+") "+str(item))


	return
















# prints a dictionary items like: key=>val
def printDict(user_dict):


	for key,val in user_dict.items():

		print(str(key)+"=>"+str(val))


	return
















def createNewFile(file_path, text=""):
	"""This method will create the path first and then create new file
	It doesn't care if the file is already present or not"""


	file_name = file_path.split("/")[-1]

	dir_path = file_path.replace(file_name, "")

	createDirIfNotPresent(dir_path)


	with open(file_path, "w+") as f:

		f.write(text)



	return




















def createDirIfNotPresent(dir_path):
	"""create directory if doesn't exist already.
	
	This method will create the whole dir_path if doesn't exist.
	Example:
	--------
	dir_path = /home/usr/nightmare/project
	
	(1) if project/ doesn't exist in /home/usr/nightmare/, 
		this method will create it.
	(2) if nightmare/ doesn't exist in /home/usr/,
		this method will create nightmare/ and then project/ inside it. 
	"""


	dir_already_present = False

	if os.path.isdir(dir_path):

		dir_already_present = True

	else:

		Path(dir_path).mkdir(parents=True, exist_ok=False)



	return dir_already_present




















def createFileIfNotPresent(file_path, data=""):
	"""create file if doesn't exist already.

	This method will create the whole file_path if doesn't exist.
	Example:
	--------
	file_path = /home/usr/nightmare/project.txt
	
	(1) if project.txt doesn't exist in /home/usr/nightmare/, 
		this method will create it.
	(2) if nightmare/ doesn't exist in /home/usr/,
		this method will create nightmare/ and then project.txt inside it. 	
	"""


	file_already_present = False


	if os.path.isfile(file_path):

		file_already_present = True



	else:

		createNewFile(file_path, data)



	return file_already_present



















def getUniqueOrderedList(any_list):
	"""This method will take any list and return a list 
	with unique data, but ordered unline built-in set method
	"""


	return list(dict.fromkeys(any_list))
















def getOnlyUniqueItems(list1, list2):
	"""This method takes two lists of data and if both of the
	lists are non-empty, it will return only the unique items
	present in list1
	"""


	unique_list1 = []

	if len(list1)>0 and len(list2)>0:


		for item in list1:


			if item not in list2:

				unique_list1.append(item)



	else:

		unique_list1 = list1




	return unique_list1


