dic = {}
n = int(input("enter a No. of element : "))
for i in range(n):
    k = input("enter key :") 
    v = input("enter value:") 
    dic.update({k:v})
print(dic)