def isLeap(y):
    if y%4==0:
        print(f"{y} is a Leap Year ")
    else:
        print(f"{y} is not Leap Year ")

for i in range(1990,2060):
    if i%4==0:
        print(i,end=",") 