#Q1. Write a Python script to merge two Python dictionaries

#Creating 2 dictionaries
dict1={'s':1,'h':2,'e':3,'f':4}
dict2={'b':5,'c':6,'d':7,'a':8}

res = {**dict1,**dict2}
print("After merge: ",res)
