

for i in range(6):
    for j in range(i-1,i):
        print(j*"*")

for i  in range(5,0,-1):
    for j in range(i,i+1):
        print(j*"*")

print("hill pattern ")
limit=int(input('enter no of rows:'))
for i in range (1,limit+1):
    for j in range(limit-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print("*",end=' ')
    print()


limit=int(input("enter number rows: "))
for i in range(limit+1,0,-1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
