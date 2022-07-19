from ast import Pass
import string
import random
set1 = string.ascii_lowercase
set2 = string.ascii_uppercase
set3 = string.digits
set4 = string.punctuation

Plen =int(input("enter a length of your password : "))
PassL=[]
PassL.extend(set1)
PassL.extend(set2)
PassL.extend(set3)
PassL.extend(set4)
print(PassL)
random.shuffle(PassL)
# print(Pass)
pString = "".join(PassL[:Plen])
print(pString)