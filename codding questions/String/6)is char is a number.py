def isnum(cr):
    for i in cr:    
        if i not in '1234567890':
            return f"{cr} is not a number charactor"
        else:
            return f"{cr} is a number charactor"
            

cr = input("enter a charactor : ")
print(isnum(cr))