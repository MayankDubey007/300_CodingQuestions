# st = 'mayank'
st = [1,1,1,1,12,2,2,2,2,23,3,3,3]
dic = {}
for i in st:
    if i in dic:
        dic[i] = dic[i]+1
    else:
        dic[i]=1
# res = max(dic,key=dic.get)
# print(res)
print(dic)