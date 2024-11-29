'''
Author:Litty jomon
description:Program to check whether the given number is a valid mobile number or not using functions.
'''
def mobile_number(num):
    if len(num)==10 and num[0] in "987":
        return True
    return False
number=input("Enter a mobile:")
if mobile_number(number):
    print(f"the number is {number} is valid")
else:print(f"the mobile number is {number} is invalid")

