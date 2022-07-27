def alp2num(st):
    ls=[]
    for i in range(len(st)):
        ls.append(ord(st[i])-96)
    return ls
def arngNM(ls):
    for i in range(len(ls)):
        for j in range(i,len(ls)):
            if ls[i]>ls[j]:
                ls[i],ls[j] = ls[j],ls[i]
    return ls
def ana(st1,st2):
    a = arngNM(alp2num(st1))
    b = arngNM(alp2num(st2))
    print(f"{st1} and {st2} are both",f"anagram" if a==b else f"not anagram")
ana("bca","abbc")
