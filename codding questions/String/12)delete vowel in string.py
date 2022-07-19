from pickletools import string1


def del_v(st):
    st1=''
    for i in st:
        if i in 'aeiou':
            st1+=""
        else:
            st1+=i
    return st1
st = input("enter a string : ")
print(del_v(st))