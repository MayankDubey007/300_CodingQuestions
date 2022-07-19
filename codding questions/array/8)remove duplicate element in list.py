arr = [2,2,2,2,6,8,6,6,2]
unq = []
for i in arr:
    if i not in unq:
        unq.append(i)
print(unq)