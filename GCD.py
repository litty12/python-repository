'''
Author:litty jomon
description:Recursive function to multiply two positive numbers
'''
def gcd(num1,num2):
    if  num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))

gcd(num1,num2)

print(gcd(num1,num2))