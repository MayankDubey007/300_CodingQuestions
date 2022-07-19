# 1
print(bin(2).replace('0b',''))
# 2
def b2d(n):
    if n>=1:
        b2d(n//2)
    print(n%2,end="|")
b2d(2)
