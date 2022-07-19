n = int(input("enter a no of rows : "))
for rows in reversed(range(1,n+2)):
    for cols in range(1,rows+1):
        print('*',end=" ")
    print() 
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print('*',end=" ")
    print() 