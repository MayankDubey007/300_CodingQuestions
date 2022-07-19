ls = [1,2,3,4,5,6,7,8,9,10]
ls2 = []
for i in range(len(ls)):
    if ls[i]%2 != 0:
        ls2.append(ls[i])
print(ls2)