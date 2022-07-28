# 2nd lrg num
ls = [1,2,3,4,5,234,23,524,8,57,4567,476,7,8,9]
max = float('-inf')
max2 = float('-inf')
for i in range(len(ls)):
    if ls[i]>max:
        max2=max
        max=ls[i]
print(max2)
