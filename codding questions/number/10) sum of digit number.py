# n = int(input("enter a number : "))
# total=0
# while n!=0:
#     total+=n%10
#     n//=10
# print(total)
# using recursion


n = int(input("enter a number : "))
def add(n,temp):
    if n==0:
        return temp
    else:
        temp += n%10
        return(add(n//10,temp))
print(add(n,0))