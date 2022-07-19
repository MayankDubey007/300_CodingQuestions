a = int(input("enter  number a :")) 
b = int(input("enter  number b :")) 
c = int(input("enter  number c :")) 
if a<=b and a<=c:
    print(f"{a} is smallest Number")
elif b<=a and b<=c:
    print(f"{b} is smallest Number")
else:
    print(f"{c} is smallest Number")