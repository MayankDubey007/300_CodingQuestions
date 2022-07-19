def IsStringAnagram(s1,s2):
    if len(s1)!=len(s2):
        print("not anagram")
        exit()
    else:
        for i in s2:
            if i not in s1:
                print("its not a anagram")
                exit()
    print("these are anagram strings")

s1 = input("enter the value of First String : ")
s2 = input("enter the value of Second String : ")
IsStringAnagram(s1,s2)
