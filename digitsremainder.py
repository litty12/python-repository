'''
author litty jomon
date25 10 2024

'''
number =int(input("enter the number"))
sum_of_digits=0
while number>0:
    remainder = number%10
    sum_of_digits = sum_of_digits+remainder
    number = number//10
print("sum of digits of the given number:",sum_of_digits)