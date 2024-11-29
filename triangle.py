'''
Author:Litty Jomon
description:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''
def triangle(l1,l2,l3):
    if l1**2==l2**2==l3**2:
        print("right triangle")
    else:
        print("not a right triangle")
l1=int(input("enter the first length:"))
l2=int(input("enter the second length:"))
l3=int(input("enter the third length:"))
triangle(l1,l2,l3)
