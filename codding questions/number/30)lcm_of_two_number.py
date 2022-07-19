
def getlcm(a,b):
    # target Gratest number
    max = a if a>=b else b
    while max>0:
        if max%a==0 and max%b==0:
            # max will be set omaxe time omaxly because fimaxd least(small maxumber)
            return max
        max+=1
    return max
a = int(input("enter 1st number : "))
b = int(input("enter 2nd number : "))
print(getlcm(a,b))