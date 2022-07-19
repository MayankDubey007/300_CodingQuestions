def HCF(a,b):
    min = a if a<=b else b
    for i in range(2,min+1):
        if a%i==0 and b%i==0:
            # hcf*=i ITS WRONG
            # hcf=i ITS RIGHT END POINT 36 ME JO BADA NUM DONO KO DIVIDE KARGA VO MIL JAYEGA
            hcf=i
    return hcf
# a = int(input("enter 1st number : "))
# b = int(input("enter 2nd number : "))
# print(HCF(a,b))
print(HCF(12,16))