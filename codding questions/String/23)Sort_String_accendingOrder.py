st="BCA"
num=[]
final=""
for i in st:
    num.append(ord(i))
for j in reversed(range(150)):
    if j in num:
        final+=chr(j)
print(final)