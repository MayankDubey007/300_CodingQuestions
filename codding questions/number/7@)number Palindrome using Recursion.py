n = int(input("enter a number : "))
def plnd(n,rev):
    if n==0:
        return rev
    rev = rev*10 + n%10
    return plnd(n//10,rev)
print(f"{n} is palindrome" if n==plnd(n,0) else f"{n} is not palindrome")























# def plnd(n, rev):
#     print("n->",n) 
#     if (n == 0):
#         return rev

#      # stores the reverse of a number
 
#     rev = (rev * 10) + (n % 10)
#     print("rev->",rev) 
#     return plnd(n // 10, rev)

# # Driver Code
# n = 121
# rev = plnd(n, 0)

# if (rev == n):
#      print("yes")
# else:
#      print("no")

# # This code is contributed
# # by mits
