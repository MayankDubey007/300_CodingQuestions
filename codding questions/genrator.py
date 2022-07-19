def fun():
    ls = [1,2,3,4,5,6]
    for i in ls:
        yield i
a = fun()
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def fun1(n): 
    for i in range(1,n+1):
        yield i*i
b = fun1(3)
print(next(b))
print(next(b))
print(next(b))