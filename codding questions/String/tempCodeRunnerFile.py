st = 'mayank'
dic = {}
for i in st:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
res = max(dic,key=dic.get)
print(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
