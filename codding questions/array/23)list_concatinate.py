# 1st way
dgt = [1,2,3,4,5,6,7,8,9,10]
alp = ['a','b','c','d','e','f','g','h','i','h']
dgt = dgt + alp
print(dgt)
# 2nd way
dgt1 = [1,2,3,4,5,6,7,8,9,10]
alp1 = ['a','b','c','d','e','f','g','h','i','h']
dgt1.extend(alp1)
print(dgt1)