
'''
author Litty jomon
date 25 10 2024
descriptionPython program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
'''
number1 = int(input("enter the first number1"))
number2 = int(input("enter the first number2"))
number3 = int(input("enter the first number3"))
if number1>number2 and number1>number3:
      print(number1,"is greater than the other two")
elif number2>number3:
    print(number2,"is greater than the other two")
else:
    print(number3,"is greater than the other two")