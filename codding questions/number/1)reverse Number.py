n=(int(input("Enter a Number For Print Reverse ")))
rev=0
while n!=0:
    rev = rev*10 +n%10
    n = n//10
print(rev)
    
