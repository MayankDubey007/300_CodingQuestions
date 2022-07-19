st = input("enter a string")
def replace(st):
    st1=""
    for i in st:
        if i!=" ":
            st1+=i
    return st1
print(replace(st))
