a = int(input("enter a first number "))
b = int(input("enter a second number "))
c = int(input("enter a third number "))

if a<=c and b<=c:
    print(c,"greattest Number") 
elif a<=b and c<=b:
    print(b,"greattest Number") 
elif c<=a and b<=a:
    print(a,"greattest Number") 