def sumIntInNum(st):
    sum=0
    for i in st:
        if i.isdigit():
            sum+=int(i)
    return sum
st = input("enter number inside String : ")            
print(sumIntInNum(st))