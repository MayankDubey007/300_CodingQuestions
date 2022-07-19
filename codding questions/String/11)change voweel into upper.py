def vowel2upper(st):
    st1=''
    for i in st:
        if i in 'aeiou':
            st1+= chr(ord(i)-32)
        else:
            st1+=i    
    return st1
st = input("enter string :")
print(vowel2upper(st))