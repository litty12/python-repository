temp = int(input("Enter temperature:"))
while True:

    print("1.\tconvert celsious to farehnheit")
    print("2.\tconvert farehnheit to celsious")
    print("3.\texit")
    choice=int(input("Enter your choice:"))
    if choice ==1:

      f=(temp* 9/5) + 32

      print(temp, "Celsious is",f,"Farehnheit")
    elif choice==2:
        c=(5/9*(temp-32))
        print(temp, "Farehnheit is",c,"Celsious")
    else:
        print("Invalid data")

