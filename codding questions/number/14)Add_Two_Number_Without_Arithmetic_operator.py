def Add(x, y):
    while (y != 0):
        carry = x & y 
        print("_1_carry->","(",carry,")",bin(carry),"x->","(",x,")",bin(x),"y->","(",y,")",bin(y))
        x = x ^ y
        print("_2_x->","(",x,")",bin(x),"y->","(",y,")",bin(y))
        y = carry << 1
        print("_3_y->","(",y,")",bin(y))
    return x
print(Add(1,2))

# def add(a,b):
#     while b!=0:
#         c = a & b
#         a = a ^ b
#         b = c<<1
#     return a
# print(add(2,5))