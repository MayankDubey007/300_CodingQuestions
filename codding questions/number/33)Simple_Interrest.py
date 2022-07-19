def si(p,r,t):
    si = (p*r*t)/100
    return si
p = int(input("enter value of principal : "))
r = int(input("enter value of rate : "))
t = int(input("enter value of time : ")) 
print(si(p,r,t))