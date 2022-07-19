def frt_vowel_rpl(st):
    st1=''
    flag=0
    for i in st:
        if i in '''aeiuoAEUOI''' and flag<1:
            st1+="-"
            flag+=1
        else:
            st1+=i
    return(st1)
st= input("enter a number : ")
print(frt_vowel_rpl(st))