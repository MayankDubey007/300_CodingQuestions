def Clist(n):
    list1 = []
    for i in range(n):
        ele = int(input(f"{i+1} number : "))
        list1.append(ele) 
    # print(list1)
    return list1
def avg(ls):
    sum=0
    for i in ls:
        sum+=i
    avg = sum//n
    print()
    return avg
n = int(input("enter length : "))
ls = Clist(n)
av = avg(ls)
print(av)

# print(avg(Clist(n)))