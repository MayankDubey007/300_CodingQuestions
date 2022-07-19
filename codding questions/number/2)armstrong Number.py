# n = int(input("enter a a number"))
# def isarmstrongF(n):
#     n1=n2=n    
#     count=total=0
#     for j in str(n):
#         count+=1
#     for i in str(n1):
#         num = int(i) ** count
#         total+=num
#     print(total)
#     if total==n:
#         print(f"{n} is a armstrong number")
#     else:
#         print(f"{n} is not a armstrong number")
# isarmstrongF(n)
    

# ...................................................
n = int(input("enter a a number"))
def isarmstrongW(n):
    n1=n2=n    
    count=total=0
    while n2!=0:
        n2=n2//10
        count+=1
    while n1 > 0:
        num = n1%10
        q = num ** count 
        n1 =n1//10
        total+=q   
    # print(total)
    if total==n:
        print(f"{n} is a armstrong number")
    else:
        print(f"{n} is not a armstrong number")
isarmstrongW(n)
    
