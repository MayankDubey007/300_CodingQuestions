st = 'mayank'
dic = {}
for i in st:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
for i in dic:
    if dic[i]==1:
        print(i,end=",")
    
        
# res = min(dic,key=dic.get)
# print(res)