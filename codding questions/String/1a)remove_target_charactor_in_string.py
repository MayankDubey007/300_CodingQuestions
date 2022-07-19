# 1)are you speaking from amazon company
# 1)are you looking for a full stack web developer
def specialAlphRemove(st,c):
    st1=''
    for i in st:
        # if i!=c:
        if i not in '''!@#$%^&*()_+=-'"<>?:''':
            st1+=i
    return st1
st = input('enter value of String -> ')
c =  input('enter value of alpha target -> ')
print(specialAlphRemove(st,c))