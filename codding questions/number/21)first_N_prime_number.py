
def isP(num):
    ls1=[]
    for i in range(1,num**2):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            if len(ls1) != num:
                ls1.append(i)
    return(ls1)
n = int(input("enter how many first prime Numbers you want :"))

print(isP(n))
    