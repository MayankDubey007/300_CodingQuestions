
def Ispalindrome(s1):
    var1=''
    for i in range(len(s1)-1,-1,-1):
        var1 += s1[i]
    if var1==s1:
        return f"strings are palindrome"
    else:
        return f"strings are not palindrome"
        
s1 = input("string 1 : ")    
print(Ispalindrome(s1))

# s = input("enter value : ")
# var1 = input("enter ")
# var2 = input("enter ")
# print(var1)
# print(s)
# print("this string is palindrome" if s!=var1 else "this not string is palinfrome")