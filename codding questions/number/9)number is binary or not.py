def chk(num):
    while num>0:
        if num%10==0 or num%10==1:
            pass
        else:
            return 0
        num = num//10
    return 1
if chk(100):
    print("Yes it is binary number")
else:
    print("It is not binary number")

