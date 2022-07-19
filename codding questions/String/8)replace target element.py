
def Replace(s,t,r):
    s1=''
    for i in s:
        if i==t:
            s1+=r
        else:
            s1+=i
    return s1
            
s = input("enter String : ")
t = input("enter Target : ")
r = input("enter Replace : ")
print(Replace(s,t,r))
