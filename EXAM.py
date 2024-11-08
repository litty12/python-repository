'''
author Litty jomon
date 08/11/2024
description :programme to find the largest and smallest numbers
'''
limit=int(input("enter a limit"))
num=int(input("enter a number"))
small=num
big=num
while limit>1:
    num=int(input("enter a number"))
    if num>big:
        big=num
    elif num<small:
        small=num
    limit=limit-1
print(f"Big={big}")
print(f"Small={small}")
