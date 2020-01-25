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


def createDirIfNotPresent(dir_path):
	"""create directory if doesn't exist already"""
	dir_already_present = False
	if os.path.isdir(dir_path):
		dir_already_present = True
	else:
		Path(dir_path).mkdir(parents=True, exist_ok=False)
	return dir_already_present

def createFileIfNotPresent(file_path):
	"""create file if doesn't exist already"""
	file_already_present = False
	if os.path.isfile(file_path):
			file_already_present = True
	else:
		with open(file_path, "w+") as f:
			f.write("")
	return file_already_present

def createNewFile(file_path):
	"""create a new file by removing old file"""
	with open(file_path, "w+") as f:
		f.write("")
	pass





