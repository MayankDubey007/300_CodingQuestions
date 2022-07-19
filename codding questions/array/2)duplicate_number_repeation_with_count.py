
# arr = [1,1,1,1,12,2,2,2,2,23,3,3,3]
# dic = {}
# for i in arr:
#     if i in dic:
#         dic[i]= dic[i]+1
#     else:
#         dic[1]=1
# print(dic)
arr = [1,1,1,1,12,2,2,2,2,23,3,3,3]
dic = {}
for i in arr:
    if i in dic:
        dic[i] = dic[i]+1
    else:
        dic[i]=1
# print(dic)
for i in dic:
    print(dic[i],"is repeated ",i,"times")