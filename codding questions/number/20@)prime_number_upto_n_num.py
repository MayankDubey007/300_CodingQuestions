def prime_N_up2_N(fn):
    # print("1,2,3",end=",")
    for i in range(1,fn):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i,end=",")
                    
fn = int(input("enter range Of prime Number :"))
prime_N_up2_N(fn)
