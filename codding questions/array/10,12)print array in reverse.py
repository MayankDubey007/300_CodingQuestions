ls = [12,3,453,64,5,3,67,7,56,2,34]
ls2=[]
for i in range(len(ls)-1,-1,-1):
    ls2.append(ls[i])
print(ls2)
# 2nd way
for i in reversed(ls):
    print(i,end=",")
# 3rd way
print()
ls.reverse()
print(ls)
# 4th way
print(ls[::-1])