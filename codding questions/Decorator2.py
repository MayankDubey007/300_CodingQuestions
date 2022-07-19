def dcor(fun):
    def inner():
        a = fun()
        a = a+5
        return a
    return inner
@dcor
def num():
    return 10

print(num())