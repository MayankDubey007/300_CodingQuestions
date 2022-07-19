def RdupE(st):
    st1=""
    for i in st:
        if i not in st1:
            st1+=i
    return st1
st = input("enter string : ")
print(RdupE(st))