# perfact means 
# a number is equal to sum of his factor
#   num = factors
# ex 28 = 1,2,4,7,14 
# 1+2+4+7+14 = 28
# if sum of factors == num then this is perfact number
def perfactChecker(n):
    nums=0
    for i in range(1,(n//2)+1):
        remain = n%i
        if remain == 0:
            # print(nums)
            nums+=i
    return nums
n = int(input("enter a number : "))
print(f"{n} is a prime number " if perfactChecker(n)==n else f"{n} is not a prime number")
