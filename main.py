def factorial(x):
    if x==1 or x==0:
        return 1 
    else:
        return(x*factorial(x-1))

num = int(input("Enter a number: "))
result=factorial(num)
print("factorial of",num,"is",result)

