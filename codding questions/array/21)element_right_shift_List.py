ls = [1,2,3,4,5,6,7,8,9,10]
ls1=[]
swp=5
for i in range(len(ls)-swp,len(ls)):
    ls1.append(ls[i])
# print(ls1)
for i in range(len(ls)-swp):
    ls1.append(ls[i])
print(ls1)
