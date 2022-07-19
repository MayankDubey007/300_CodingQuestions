ls = [1,2,3,4,5,6,7,8,9,10]
ls1=[]
swp = 3
for i in range(swp,len(ls)):
    ls1.append(ls[i])
for i in range(swp):
    ls1.append(ls[i])
print(ls1)