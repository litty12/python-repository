'''
author litty
date 18 10 2024
descriptionCreate, concatenate, and print a string and access a sub-string from a given string.
'''
first_name = input("enter your first name")
last_name = input("enter your last name")
name = first_name+" "+last_name
print(name)
first_name_length = len(first_name)
print(first_name_length)
extracted_last_name=name[first_name_length+1:]
print(extracted_last_name)