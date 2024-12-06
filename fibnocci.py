def fibonacci(n):
    num1=0
    num2=1
    print(num1)
    print(num2)
    for i in range(n):
        sum=num1+num2
        print(sum)
        num1=num2
        num2=sum
