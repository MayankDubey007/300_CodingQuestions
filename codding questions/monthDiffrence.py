

d1 = '2022-05' 
d2 = '2022-04'
if d1[:4]==d2[:4]:
    m1=int(d1[5:])
    m2=int(d2[5:])
    df_M = m1-m2 if m1>m2 else m2-m1
else:
    bigD = d1 if d1[:4]>=d2[:4] else d2 
    smlD = d1 if bigD>=d1 else d2
    # print(smlD)
    bigD_Y= int(bigD[:4])
    bigD_M= int(bigD[5:])
    smlD_Y= int(smlD[:4])
    smlD_M= int(smlD[5:])

    if smlD_M<=bigD_M:
        df_M = (bigD_Y-smlD_Y)
        df_M = (bigD_M-smlD_M)+(12*df_M)
    else:
        df_M = (bigD_Y-smlD_Y)-1
        df_M = ((bigD_M + 12) - smlD_M)+(df_M*12)

    
    
print(df_M)