'''
author litty
date:18 10 24
descriptionPython program that uses functions from the math module to perform the following operations on a number provided by the user:


'''
import math
number=int(input("enter a number:"))
square_root=math.sqrt(number)
print("Square root of",number,":",square_root)
factorial=math.factorial(number)
print("factorial of number",number,":",factorial)
power=math.pow(number,2)
print("power of number",number,":",power)