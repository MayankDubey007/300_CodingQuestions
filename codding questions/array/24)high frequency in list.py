ls = [2,1,2,1,2,12,1,2,3,1,2,4,5,6,7,8]
dic = {}
for i in ls:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
# max()
print(dic)
print(max(dic,key=dic.get))