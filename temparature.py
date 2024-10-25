'''
Author litty
date 25 10 2024
descriptionPython program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:

'''
temparature=int(input("enter temparature"))
unit=(input("is this in (C)elsious or (F)arehnheit "))
if unit=="C":
    f = (9/5*temparature) + 32
    print(temparature,"Celsious is",f,"faehnheit")
else:
    c=5/9*(temparature-32)
    print(temparature,"farehnheit is",c,"celsious")