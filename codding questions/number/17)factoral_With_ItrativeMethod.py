def factorial(n):
    sum=1
    for i in range(n,0,-1):
        sum*=i
    return sum
print(factorial(int(input("enter a a number :"))))