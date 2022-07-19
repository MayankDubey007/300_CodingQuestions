def countOccurence(s,c):
    cnt = 0
    for i in s:
        if i==c:
            cnt+=1
    return cnt
s = input("enter String : ")
c = input("enter Char : ")
print(countOccurence(s,c))