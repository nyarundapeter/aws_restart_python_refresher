"""
Python List Data Type
-------------------------
This script demonstrates the flexibility of Python lists by  
including elements of different data types and printing their types.

"""

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
    
