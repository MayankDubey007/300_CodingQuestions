def IsNumPalind(num):
    n1=num
    rev = 0
    while n1!=0:
        rev = rev*10 + n1%10
        n1= n1//10
    p = f"{num} is a palindrome Number" if num==rev else f"{num} is Not a palindrome Number"
    print(p)
    
IsNumPalind(122)