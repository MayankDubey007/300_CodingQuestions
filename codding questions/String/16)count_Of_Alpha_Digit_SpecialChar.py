
st = input("enter a string :")
dgt=0
alp=0
sc=0
for i in st:
    if i.isdigit():
        dgt+=1
    elif i.isalpha():
        alp+=1
    else:
        sc+=1
print("count of special charactor",sc)
print("count of digit number",dgt)
print("count of alphabetic charactor",alp)
