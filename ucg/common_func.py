#!/usr/bin/python3
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


def createNewFile(file_path):
	"""This method will create the path first and then create new file
	It doesn't care if the file is already present or not"""
	file_name = file_path.split("/")[-1]
	dir_path = file_path.replace(file_name, "")
	createDirIfNotPresent(dir_path)
	with open(file_path, "w+") as f:
		f.write("")
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

def createFileIfNotPresent(file_path):
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
		createNewFile(file_path)
	return file_already_present




