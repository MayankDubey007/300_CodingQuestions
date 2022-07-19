ls = [9,7,5,644,6,2,5,68,25,737,3]
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            ls[i],ls[j] = ls[j],ls[i]
            
print(ls)