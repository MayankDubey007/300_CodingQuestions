# def IsPrime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print(f"{n} is not Prime Number")
#             exit()
#         else:
#             print(f"{n} is a prime Number")
#             exit()
# n = int(input("enter a number :"))
# print(IsPrime(n))
from itertools import count


def IsPrime(n):
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not Prime Number")
            continue
        else:
            print(i,end=",")

n = int(input("enter a number :"))
print(IsPrime(n))