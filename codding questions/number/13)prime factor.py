# def primefact(n):
#     while n%2==0:
#         print(2,end=",")
#         n//=2
#     while n%3==0:
#         print(3,end=",")
#         n//=3
#     if n>3:
#         print(n)

# n = int(input("enter a number : "))
# primefact(n)

def prF(num):
    while num%2==0:
        print(2,end=",")
        num = num//2
    while num%3==0:
        print(3,end=",")
        num = num//3
    if num>3:
        print(num,end=",")
prF(28)
            