def RemoveSpecialChar(s):
    new_s=""
    for i in s:
        if i not in '''!@#$%^&*()_+}{:"<?><":}{\|''':
            new_s += i
    return new_s
s = input("enter a String  : ")
print(RemoveSpecialChar(s)) 