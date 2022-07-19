# arr = []
# n = int(input("enter size of array : "))
# for x in range(n):
#     x=int(input("enter element of array : "))
#     arr.append(x)

def getMissingNo(A):
    n = len(A)
    sm=0
    total = (n + 1)*(n + 2)/2
    for i in A:
        sm+=i
    # print(sm)
    return total - sm
#  .............................................................
arr = [2, 3, 4, 5, 6]
miss = getMissingNo(arr)
print(miss)


# ls = [2,3,4,5,6]
# l = len(ls)
# sum = (l+1)*(l+2)/2
# Lsum=0
# for i in ls:
#     Lsum+=i
# print("no missing any number " if sum-Lsum==ls[-1]+1 else sum-Lsum)
