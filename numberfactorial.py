'''
Author:Litty jomon
description:Program to find the factorial of a number using Recursion.
'''
def factorial(n):
    if n==0:
      return 1
    else:
        return(n*factorial(n-1))
n=int(input('Enter a number:'))
print('factorial of',n,':',factorial(n))


