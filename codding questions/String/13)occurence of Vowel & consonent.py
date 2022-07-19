

def occurenceOfV_C(st):
    v=0
    c=0
    for i in st:
        if i not in'''1234567890!@#$%^&*()+_) ]\/[}{;'":-=''':
            if i in 'aeuio':
                v+=1
            else:
                # print(i,end=",")
                c+=1
    return f"vowel = {v}\nconsonent {c}"
st = input("enter a string : ")
print(occurenceOfV_C(st))