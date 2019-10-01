#!/usr/bin/python3
"""
Function List:
1) printList(user_list)
		prints items of list one by one
2) printListN(user_list)
		prints items of a list one by one and numbered
3) printDict(user_dict)

"""




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



