def isWhat(s):
    if s in 'aeiouAEIOU':
        return f"entered char {s} is Vowel"
    else:
        return f"entered char {s} is Consonent"
        
s = input("enter a Char : ")
print(isWhat(s))