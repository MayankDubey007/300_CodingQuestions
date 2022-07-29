
3# find missing number in python 
# ............................................
ls = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17,]
# ls = [1, 2, 4, 5]
print(ls)
def misN(ls):
    ln = len(ls)
    gen_sum=0
    sum=0
    for i in range(len(ls)):
        gen_sum+=(i+1)
        sum+=ls[i]
    # print(gen_sum)
    # print(sum)
    # print(sum-(gen_sum-1))
    return sum-(gen_sum-1)
print(misN(ls))
