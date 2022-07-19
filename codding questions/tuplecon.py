ls1 = [1,2,3,4]
print(id(ls1))
ls2 = [5,6,7,8]
print(id(ls2))
# 
ls3 = ls1.extend(ls2)
print(id(ls3))

# ....................
# l